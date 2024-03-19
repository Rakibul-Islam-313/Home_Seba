from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms
# Create your views here.

class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = forms.RegistrationForm

    def get(self,request):
        registar_form = self.form_class()
        return render(request,self.template_name,{'form':registar_form,})
    def post(self,request):
        registar_form = self.form_class(request.POST)
        if registar_form.is_valid():
            registar_form.save()
            messages.success(request,'Registration Successful')
            return redirect('login_view')
        return render(request, self.template_name,{'form':registar_form})

class loginView(LoginView):
    template_name = 'login.html'
    form_class = forms.AuthenticationForm

    def get(self,request):
        login_form = self.form_class()
        return render(request,self.template_name,{'form':login_form})
    def post(self,request):
        login_form = self.form_class(request=request, data=request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=name,password=user_pass)
            if user is not None:
                login(request,user)
                messages.success(request, 'login successful')
                return redirect('create_profile')
        return render(request, self.template_name, {'form':login_form})

class logoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home_view')