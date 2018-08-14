#!/usr/bin/env python

import asyncio
import os

import websockets


@asyncio.coroutine
async def ws_handler(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    response = '\r\n'.join([
        'HTTP/1.1 200 OK',
        'Content-Type: text/json',
        '',
        '' + '{"version":"1.0","sessionAttributes":{},"response":{"outputSpeech":{"type":"PlainText","text":"There are 3 atm"},"shouldEndSession":true}}' + '',
    ])

    await websocket.send(response)
    print(f"> {response}")


port = int(os.getenv('PORT', 8765))  # 8765
start_server = websockets.serve(ws_handler, '', port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
