from django.shortcuts import render 
from Services.models import HomeServices
def home(request):
    return render(request,'home.html')

def Service(request):
    data = HomeServices.objects.all()
    return render(request,'services.html',{'data':data,})

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')