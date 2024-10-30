import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import SnackSpot
from channels.db import database_sync_to_async

logger = logging.getLogger(__name__)

class SnackConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            await self.accept()
            logger.info("WebSocket connection accepted.")
        except Exception as e:
            logger.error(f"Error in connect: {e}")

    async def disconnect(self, close_code):
        # Handle disconnection logic here
        logger.info(f"WebSocket disconnected with code {close_code}.")

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            if data.get('action') == 'decrement':
                snack_id = data.get('snack_id')
                snack = await self.get_snack(snack_id)
                if snack and snack.amount > 0:
                    snack.amount -= 1
                    await self.update_and_broadcast(snack)
        except Exception as e:
            logger.error(f"Error in receive: {e}")

    async def update_and_broadcast(self, snack):
        await database_sync_to_async(snack.save)()
        await self.send(text_data=json.dumps({
            'snackId': snack.id,
            'newAmount': snack.amount
        }))

    @database_sync_to_async
    def get_snack(self, snack_id):
        return SnackSpot.objects.get(id=snack_id)
