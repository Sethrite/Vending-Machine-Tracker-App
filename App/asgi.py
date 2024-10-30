import os
import django
import logging

# Set the DJANGO_SETTINGS_MODULE environment variable first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')

# Initialize Django before importing get_asgi_application
django.setup()

# Now import the ASGI application and Channels components
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from playground.routing import websocket_urlpatterns

# Get the default Django ASGI application
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

# Initialize logging
logger = logging.getLogger(__name__)
logger.info("ASGI application initialized")
