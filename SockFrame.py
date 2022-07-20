import websockets
import asyncio


class SocketHandler:
	def __init__(self, address:str, port:int=8765):
		self.address = address
		self.port = port

	def reciever(self, type, func):
		def inner(wsmessage):
			func(wsmessage)
		return inner

	async def handler(self, websocket):
		while True:
			message = await websocket.recv()
			await websocket.send(message)

	async def main(self):
		async with websockets.serve(self.handler, self.address, self.port):
			await asyncio.Future()

	def run(self):
		asyncio.run(self.main())
	