import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CodeEditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = f"code_editor_{self.room_code}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        code = text_data_json['code']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'code_message',
                'code': code
            }
        )

    async def code_message(self, event):
        code = event['code']

        await self.send(text_data=json.dumps({
            'code': code
        }))
