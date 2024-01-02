import json

from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .models import SoilSensorData


class DataConsumer(AsyncWebsocketConsumer):

    def get_data(self):
        return SoilSensorData.objects.all()

    async def connect(self):

        data = await database_sync_to_async(self.get_data)()

        await self.accept()
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Connected'
        }))
