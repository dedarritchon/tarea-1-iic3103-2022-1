import asyncio
import websockets
import json
from main import User
from utils import USERS

async def main():
    nodes = [User(id=f"test_{k}", username=v.replace(' ', '_')) for k, v in USERS.items()][:3]
    await asyncio.gather(
        *[n.join_network() for n in nodes]
    )

if __name__ == "__main__":
    asyncio.run(main())
