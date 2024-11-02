# playground/tasks.py
from celery import shared_task
from .models import SnackSpot
import random
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def decrement_snack_spots():
    snacks = SnackSpot.objects.all()
    if snacks:  # Check if there are any snacks
        random_snack = random.choice(snacks)  # Choose a random snack
        new_amount = random_snack.decrement_amount()  # Decrement the amount of the random snack

        # Log the ID of the decremented snack
        print(f"Decremented snack: {random_snack.id}, New amount: {new_amount}")

        # Send an update to the WebSocket group for this snack
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(  # Sending message to the group
            f'vending_machine_{random_snack.id}',  # Assuming the group name includes the snack ID
            {
                'type': 'send_update',  # The method in your consumer to handle the update
                'snackId': random_snack.id,
                'newAmount': new_amount,  # Pass the new amount after decrementing
            }
        )
