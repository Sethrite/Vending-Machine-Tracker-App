from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/User/vending-machine/(?P<snack_id>\d+)/$', consumers.SnackConsumer.as_asgi()),
    re_path(r'ws/Manufacturer/vending-machine/(?P<snack_id>\d+)/$', consumers.SnackConsumer.as_asgi())
]
