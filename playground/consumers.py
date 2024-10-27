# playground/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SnackConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # You can send an initial message here if needed
        await self.send(json.dumps({'message': 'Connected to snack updates.'}))

    async def disconnect(self, close_code):
        # Handle disconnection logic here
        pass

    async def send_snack_update(self, snack_data):
        # This method can be called to send updates to the client
        await self.send(text_data=json.dumps(snack_data))
