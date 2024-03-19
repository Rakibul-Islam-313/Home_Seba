from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms 
from . import models 
# Create your views here.
    
# class ProfileCreateView(CreateView):
#     template_name = 'profile_form.html'
#     form_class = forms.ProfileForm

#     def get(self,request):
#         create_profile = self.form_class()
#         return render(request,self.template_name,{'form':create_profile})
    
#     def post(self,request):
#         create_profile = self.form_class(request.POST)
#         if create_profile.is_valid():
#             print("hi")
#             create_profile.save()
#             messages.success(request,'profile creation successful')
#             return redirect('profile_page')
#         return render(request,self.template_name,{'form':create_profile})

# class ProfileCreateView(CreateView):
#     template_name = 'profile_form.html'
#     form_class = forms.ProfileForm
 
#     def get(self, request, *args, **kwargs):
#         create_profile = self.form_class()
#         return render(request, self.template_name,{'form': create_profile})
 
#     def post(self, request, *args, **kwargs):
#         print(request.POST)
#         create_profile = self.form_class(request.POST, request.FILES)
#         if create_profile.is_valid():
#             # create_profile.instance.name = request.user
#             obj = create_profile.save(commit=False)
#             obj.name = request.user
#             obj.save()
#             messages.success(request, 'Profile creation successful')
#             return redirect('profile_page')
#         return render(request, self.template_name, {'form': create_profile})

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

class ProfileView(DetailView):
    model = models.ProfileModel
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self,queryset=None):
        return models.ProfileModel.objects.get(name=self.request.user)


def create_profile(request):
        if request.method == "POST":
            form = forms.ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.name = request.user
                obj.save()
                messages.success(request,'Profile creation successful')
                return redirect('profile_page', pk=obj.pk)
        form=forms.ProfileForm()
        return render(request,'profile_form.html',{'form': form})
           
       

    