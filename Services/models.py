from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HomeServices(models.Model):
    service_name = models.CharField(max_length = 40)
    service_detail = models.TextField()
    service_price = models.IntegerField()

    def __str__(self):
        return self.service_name 
    
RATING = [
    ('★','★'),
    ('★★','★★'),
    ('★★★','★★★'),
    ('★★★★','★★★★'),
    ('★★★★★','★★★★★'),
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(HomeServices, on_delete = models.CASCADE, related_name="comments")
    rating = models.CharField(max_length=5, choices = RATING )
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username}"

class Order(models.Model):
    client = models.ForeignKey(User, on_delete = models.CASCADE)
    service = models.ForeignKey(HomeServices, on_delete = models.CASCADE)
    is_cancelled = models.BooleanField(default = False)

    def __str__(self):
        return f"Order by : {self.client.username} => {self.service.service_name}"
