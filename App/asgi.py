"""
ASGI config for App project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from playground.routing import websocket_urlpatterns  # Adjust this import based on your actual routing file location

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')
django.setup()

# Get the default Django ASGI application
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

# Create the ASGI application
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Handle HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Your WebSocket URL patterns
        )
    ),
})
