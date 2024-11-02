import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'App.settings')  # Ensure this points to your settings module

app = Celery('App')  # You can replace 'App' with your project name

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
