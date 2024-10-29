# playground/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import SnackSpot

class SnackConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        # Handle disconnection logic here
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get('action') == 'decrement':
            snack_id = data.get('snack_id')
            snack = await self.get_snack(snack_id)
            if snack and snack.amount > 0:
                snack.amount -= 1
                await self.update_and_broadcast(snack)

    async def update_and_broadcast(self, snack):
        snack.save()
        await self.send(text_data=json.dumps({
            'snackId': snack.id,
            'newAmount': snack.amount
        }))

    @staticmethod
    async def get_snack(snack_id):
        return await SnackSpot.objects.get(id=snack_id)