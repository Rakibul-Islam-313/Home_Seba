from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView
from django.views.generic import ListView
from django.contrib import messages
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from . import models 
from . import forms  

# Create your views here.

class ServiceView(CreateView):
    model = models.HomeServices
    form_class = forms.ServiceForm
    template_name = 'home.html'

    def form_valid(self,form):
        return super().form_valid(form)

class ServiceDetails(DetailView):
    model = models.HomeServices
    template_name = 'service_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'service'

    def get_success_url(self):
        return reverse_lazy('service_detail_page',kwargs={'id':self.object.pk})
    
    def post(self, *args, **kwargs):
            comment_form = forms.ReviewForm(data=self.request.POST)
            post = self.get_object()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.service = post 
                new_comment.user = self.request.user
                new_comment.save()
                messages.success(self.request,'Thanks for nice review')
            return self.get(self, *args, **kwargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        service = self.object 
        comments = service.comments.all()
        comment_form = forms.ReviewForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context 
       

class AddCartView(ListView):
    model = models.HomeServices
    template_name = 'cart.html'
    context_object_name = 'ServiceCart'

    # def get_object(self,queryset=None):
    #     return models.HomeServices.objects.get(name=self.request.user)
    
    # pk_url_kwarg = 'id'
    # def get_success_url(self):
    #     return reverse_lazy('service_cart_page',kwargs={'id':self.object.pk})

class OrderServiceView(CreateView):
    model = models.Order
    template_name = 'profile.html'
    fields = ['client','service','is_cancelled']
    success_url = 'service_order_page'

    def form_valid(self,form):
        messages.success(self.request, 'Order taken Successfully')
        return super().form_valid(form)


    