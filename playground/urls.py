from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.Homepage),
    path('Manufacturer/', views.Manufacturer),
    path('User/', views.User),
    path('User/VendingMachine1/', views.VendingLookU),
    path('User/VendingMachine2/', views.VendingLookU),
    path('User/VendingMachine3/', views.VendingLookU),
    path('Manufacturer/VendingMachine1/', views.VendingLookM),
    path('Manufacturer/VendingMachine2/', views.VendingLookM),
    path('Manufacturer/VendingMachine3/', views.VendingLookM),
]