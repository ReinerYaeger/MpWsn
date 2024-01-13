import asyncio
import json
from random import randint

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import SoilSensorData
import plotly.express as px


class DataConsumer(AsyncWebsocketConsumer):

    def get_data(self):
        return SoilSensorData.objects.all()

    async def connect(self):
        data = await database_sync_to_async(self.get_data)()

        await self.accept()
        while True:
            one = SoilSensorData.objects.all()
            ran1 = randint(10, 20)
            ran2 = randint(10, 20)
            ran3 = randint(10, 20)

            avg = (ran1 + ran2 + ran3) / 3
            await self.send(
                json.dumps({
                    'type': 'live_sensor_data',
                    'label': 'z',
                    'message': 'contains all sensor data access by value[n]',

                    'AA': avg,
                    'A0_date': ran1,
                    'A0': ran1,
                    'A1': ran2,
                    'A1_date': ran1,
                    'A2': ran3,
                    'A2_date': ran1,
                })
            )

            await self.send(
                json.dumps({
                    'type': 'live_sensor_data',
                    'label': 'A1',
                    'message': 'contains all sensor data access by value[n]',
                    'AA': randint(-20, 20),
                    'A0': randint(-20, 20),
                    'A1': randint(-20, 20),
                    'A2': randint(-20, 20),
                })
            )
            await self.send(
                json.dumps({
                    'type': 'live_sensor_data',
                    'label': 'A2',
                    'message': 'contains all sensor data access by value[n]',
                    'AA': randint(-20, 20),
                    'A0': randint(-20, 20),
                    'A1': randint(-20, 20),
                    'A2': randint(-20, 20),
                })
            )
            await asyncio.sleep(1)


def plot_data():
    df = px.data.tips()
    fig = px.box(df, y="total_bill")
    box_plot = fig.to_html(full_html=False, include_plotlyjs=False)

    context = {
        "box_plot": box_plot
    }
    return context
