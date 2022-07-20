import websockets
import asyncio


class SocketHandler:
	def __init__(self, address:str, port:int=8765):
		self.address = address
		self.port = port
		self.Paths = {}

	def reciever(self, func):
		def wrapper():
			self.Paths[func.__name__] = func
		return wrapper

	def decorator(self, func):
		def wrappy(*args, **kwargs):
			return func(*args, **kwargs)
		return wrappy

	async def handler(self, websocket):
		while True:
			message = await websocket.recv()
			await websocket.send(message)

	async def main(self):
		async with websockets.serve(self.handler, self.address, self.port):
			await asyncio.Future()

	def run(self):
		asyncio.run(self.main())
	