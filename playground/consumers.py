import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import VendingMachine  # Assuming you have a VendingMachine model
from channels.db import database_sync_to_async

logger = logging.getLogger(__name__)

class SnackConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.machine_id = self.scope['url_route']['kwargs']['machine_id']
        self.group_name = f'vending_machine_{self.machine_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        logger.info(f"WebSocket connection accepted for machine: {self.machine_id}.")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        logger.info(f"WebSocket disconnected for machine: {self.machine_id} with code {close_code}.")

    async def receive(self, text_data):
        # Your existing logic to handle messages
        pass

    async def update_and_broadcast(self, snack):
        await database_sync_to_async(snack.save)()
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_update',
                'snackId': snack.id,
                'newAmount': snack.amount
            }
        )

    async def send_update(self, event):
        await self.send(text_data=json.dumps({
            'snackId': event['snackId'],
            'newAmount': event['newAmount']
        }))
