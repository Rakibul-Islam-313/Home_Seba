from django import forms 
from . models import HomeServices,Review

class ServiceForm(forms.ModelForm):
    class Meta:
        model = HomeServices
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comment']