# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ClassRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"class_{self.room_name}"

        # Add the user to the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Broadcast the received message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': text_data
            }
        )

    async def chat_message(self, event):
        # Send the received message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
