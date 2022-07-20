from SockFrame import SocketHandler

TheHandler = SocketHandler("localhost", 8765)

@TheHandler.reciever("message")
def message_handler(data):
	print(data)
