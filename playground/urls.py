from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.Homepage, name='home'),
    path('User/', views.User, name='user'),
    path('User/vending-machine/<int:id>/', views.VendingLookU, name='vending_lookup'),
    path('User/vending-machine/<int:id>/', views.snack_data, name='snack_data'),
    path('User/vending-machine/<int:id>/', views.increment_snack, name='increment'),
    path('User/vending-machine/<int:id>/', views.decrement_snack, name='decrement'),

    path('Manufacturer/', views.Manufacturer, name='manufacturer'),
    path('Manufacturer/vending-machine/<int:id>/', views.VendingLookM, name='vending_lookupm'),
    path('Manufacturer/vending-machine/<int:id>/', views.snack_data, name='snack_data'),
    path('Manufacturer/vending-machine/<int:id>/', views.restock_snack, name='restock'),

]