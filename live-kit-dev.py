
# Install package first
# pip install livekit-api

import asyncio
import os
from livekit.api import LiveKitAPI, CreateRoomRequest
from dotenv import load_dotenv
# Load API credentials from environment variables
load_dotenv()
LIVEKIT_URL = os.environ.get("LIVEKIT_URL")        # e.g., "https://my-livekit-server.com"
LIVEKIT_API_KEY = os.environ.get("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.environ.get("LIVEKIT_API_SECRET")

async def create_room():
    # Initialize the LiveKit API client
    lkapi = LiveKitAPI(LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET)

    # Create a new room
    room = await lkapi.room.create_room(
        CreateRoomRequest(
            name="myroom",
            empty_timeout=10*60,  # 10 minutes
            max_participants=2
        )
    )
    print("Room created:", room.sid, room.name)
    return room

# Run the async function
if __name__ == "__main__":
    asyncio.run(create_room())