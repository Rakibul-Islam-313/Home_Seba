from django.urls import path 
from . import views

urlpatterns = [
    path('service/',views.ServiceView.as_view(), name='ServiceView_page'),
    path('service_detail/<int:id>/',views.ServiceDetails.as_view(), name='service_detail_page'), 
    path('service_cart/',views.AddCartView.as_view(), name='service_cart_page'),
    path('service_order/',views.OrderServiceView.as_view(), name='service_order_page'),
]
