from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.Homepage, name='home'),
    path('User/', views.User, name='user'),
    path('User/vending-machine/<int:id>/', views.VendingLookU, name='vending_lookup'),
    path('Manufacturer/', views.Manufacturer, name='manufacturer'),
    path('Manufacturer/vending-machine/<int:id>/', views.VendingLookM, name='vending_lookupm'),

]