import asyncio
import websockets
import json
from models import VendingMachine

async def test_decrement(snack_id, machine_id):
    uri = f"ws://localhost:8000/ws/User/vending-machine/{machine_id}/"  # Use f-string for dynamic URL
    async with websockets.connect(uri) as websocket:
        # Send decrement message
        await websocket.send(json.dumps({
            "action": "decrement",
            "snack_id": snack_id
        }))

        # Receive and print response
        response = await websocket.recv()
        print("Response from server:", response)

if __name__ == "__main__":
    # Test the decrement action on a snack with snack_id=1 in a specific machine
    machine_id = 1  # Replace with the actual machine ID you want to test
    asyncio.run(test_decrement(snack_id=1, machine_id=machine_id))
