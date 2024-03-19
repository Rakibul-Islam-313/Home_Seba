from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.RegistrationView.as_view(),name='registar_view'),
    path('login/', views.loginView.as_view(), name='login_view'),
    path('logout/', views.logoutView.as_view(), name='logout_view'),
]
