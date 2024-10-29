import asyncio
import websockets
import json

async def test_decrement(snack_id):
    uri = "ws://localhost:8000/ws/snacks/"
    async with websockets.connect(uri) as websocket:
        # Send decrement message
        await websocket.send(json.dumps({
            "action": "decrement",
            "snack_id": snack_id
        }))

        # Receive and print response
        response = await websocket.recv()
        print("Response from server:", response)

# Test the decrement action on a snack with snack_id=1
asyncio.run(test_decrement(snack_id=1))
