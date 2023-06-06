import random
from channels.generic.websocket import (
    AsyncWebsocketConsumer
)

from channels.consumer import SyncConsumer, AsyncConsumer
import json
import time


class WSConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        print("polaczenie z websocket")
        print("damian")

    async def disconnect(self, code):
        await self.close()

    async def receive(self, text_data=None, **kwargs):
        print(text_data)
        data = json.dumps(text_data)
        await self.send_response("naura")

    async def send_response(self, text_data=None):
        print("Twoj stary najebany", flush=True)
        response = json.dumps({"message":text_data})
        await self.send(response)



