from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

USER_ROLES = [
    ('Admin','Admin'),
    ('Client','Client'),
]

class ProfileModel(models.Model):
    picture = models.ImageField(upload_to='clients/images/')
    name = models.OneToOneField(User, on_delete = models.CASCADE)
    status = models.CharField(max_length = 50, choices = USER_ROLES)
    bio_data = models.TextField()
    social_media_link = models.URLField()

    def __str__(self):
        return self.name.username
    

    