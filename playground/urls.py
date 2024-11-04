from django.urls import path
from . import views

# URLConf
# Updated URLConf
urlpatterns = [
    path('', views.Homepage, name='home'),
    path('User/', views.User, name='user'),
    path('User/vending-machine/<int:id>/', views.VendingLookU, name='vending_lookup'),
    path('User/vending-machine/<int:id>/snack-data/', views.snack_data, name='snack_data'),
    path('User/vending-machine/<int:id>/increment/<int:snack_id>/', views.increment_snack, name='increment'),
    path('User/vending-machine/<int:id>/decrement/<int:snack_id>/', views.decrement_snack, name='decrement'),
    
    path('Manufacturer/', views.Manufacturer, name='manufacturer'),
    path('Manufacturer/vending-machine/<int:id>/', views.VendingLookM, name='vending_lookupm'),
    path('Manufacturer/vending-machine/<int:id>/snack-data/', views.snack_data, name='snack_data'),
    path('Manufacturer/vending-machine/<int:id>/restock/', views.restock_snack, name='restock'),
    path('Manufacturer/vending-machine/reset/', views.reset_snacks, name='reset'),
    path('Manufacturer/vending-machine/<int:id>/increment/<int:snack_id>/', views.increment_snack, name='increment'),
    path('Manufacturer/vending-machine/<int:id>/decrement/<int:snack_id>/', views.decrement_snack, name='decrement'),
]
