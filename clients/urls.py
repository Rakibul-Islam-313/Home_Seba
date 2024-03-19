from django.urls import path
from . import views

urlpatterns = [
    # path('profile_create/',views.ProfileCreateView.as_view(),name='create_profile'),
    path('about/',views.About,name='about_view'),
    path('contact/',views.Contact,name='contact_view'),

    path('profile_create/',views.create_profile,name='create_profile'),

    path('profile/',views.ProfileView.as_view(), name='profile_page'),
]
