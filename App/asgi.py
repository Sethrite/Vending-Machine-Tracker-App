import os
import logging
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from playground.routing import websocket_urlpatterns

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')

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

# Initialize logging
logger = logging.getLogger(__name__)
logger.info("ASGI application initialized")
