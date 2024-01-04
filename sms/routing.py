from django.urls import path
from . import consumer

websocket_urlpatterns = [
    path('ws/socket-server/', consumer.DataConsumer.as_asgi())
]
