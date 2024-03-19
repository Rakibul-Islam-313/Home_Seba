from django import forms 
from . import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.ProfileModel
        fields = ['picture','status','bio_data','social_media_link']
