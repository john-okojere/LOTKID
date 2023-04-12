
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('add-phone/', views.addphone , name="addphone"),
    path('add-prayer/', views.addprayer , name="addprayer")
]
