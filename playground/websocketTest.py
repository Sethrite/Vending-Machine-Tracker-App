import os
import sys
import asyncio
import websockets
import json

# Add the App directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace with your actual settings module

async def test_decrement(snack_id, machine_id):
    uri = f"ws://localhost:8001/ws/User/vending-machine/{machine_id}/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({
            "action": "decrement",
            "snack_id": snack_id
        }))
        response = await websocket.recv()
        print("Response from server:", response)

if __name__ == "__main__":
    machine_id = 1  # Replace with the actual machine ID you want to test
    asyncio.run(test_decrement(snack_id=3, machine_id=machine_id))
