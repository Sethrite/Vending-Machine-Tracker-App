# tasks.py
from celery import shared_task
from .models import SnackSpot

@shared_task
def decrement_snack_spots():
    snacks = SnackSpot.objects.all()
    for snack in snacks:
        snack.decrement_amount()
