#!/usr/bin/env python

import asyncio
import os

import websockets


async def ws_handler(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


port = int(os.getenv('PORT', 80))# 8765
start_server = websockets.serve(ws_handler, '', port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
