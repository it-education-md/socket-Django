# webSocket/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Handle disconnection
        pass

    async def receive(self, text_data):
        # Handle receiving data from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Process the message (add your logic here)
        response = await self.process_data(message)
        
        # Send response back to WebSocket
        await self.send(text_data=json.dumps({
            'message': response
        }))

    async def process_data(self, data):
        # Simulate processing and return a response
        # Replace this with actual logic to interact with Unreal Engine and AI
        return "Processed data or URL from AI"
