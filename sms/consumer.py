import json

from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .models import SoilSensorData
import plotly.express as px


class DataConsumer(AsyncWebsocketConsumer):

    def get_data(self):
        return SoilSensorData.objects.all()

    async def connect(self):
        data = await database_sync_to_async(self.get_data)()

        await self.accept()
        await self.send(
            text_data=json.dumps({
                'type': 'connection_established',
                'message': plot_data()
            })
        )


def plot_data():
    df = px.data.tips()
    fig = px.box(df, y="total_bill")
    box_plot = fig.to_html(full_html=False, include_plotlyjs=False)

    context = {
        "box_plot": box_plot
    }
    return context
