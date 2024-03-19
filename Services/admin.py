from django.contrib import admin
from . import models 

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','id']
    
admin.site.register(models.HomeServices)
admin.site.register(models.Review)