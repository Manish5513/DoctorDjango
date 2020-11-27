from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name = "home"),
    path('appointment.html',views.appointment,name = "appointment"),
    path('contact.html',views.contact,name = "contact"),
    path('pricing.html',views.pricing,name='pricing'),
    path('service.html',views.service,name='service'),
     
]   