from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.Homepage),
    path('Manufacturer/', views.Manufacturer),
    path('User/', views.User)
]