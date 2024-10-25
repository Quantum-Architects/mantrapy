import asyncio

import websockets


class ChainClient:

    def __init__(self, websocket_url):
        self.websocket_url = websocket_url

    async def subscribe(self, query, max_retries=3):
        retry_count = 0
        while retry_count < max_retries:
            try:
                async with websockets.connect(self.websocket_url) as websocket:
                    await websocket.send(
                        f'{{"jsonrpc":"2.0","method":"subscribe","params":["{query}"],"id":1}}',
                    )
                    while True:
                        message = await websocket.recv()
                        yield message
            except websockets.ConnectionClosedError as e:
                print(f'Connection error: {e}. Retrying...')
                retry_count += 1
                await asyncio.sleep(2)  # Wait before retrying
            except websockets.InvalidStatusCode as e:
                print(f'Invalid status code error: {e}. Retrying...')
                retry_count += 1
                await asyncio.sleep(2)  # Wait before retrying
            except asyncio.TimeoutError:
                print('Connection timed out. Retrying...')
                retry_count += 1
                await asyncio.sleep(2)  # Wait before retrying

        print('Max reconnect attempts reached. Exiting...')
