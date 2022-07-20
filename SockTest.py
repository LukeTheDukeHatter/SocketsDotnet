from SockFrame import SocketHandler

TheHandler = SocketHandler("localhost", 8765)

# @TheHandler.decorator('aa')
# def bbb(msg):
# 	print(msg)

class temp:
	def __init__(self):
		self.Paths = {}

	def decor(self, n):
		def tmp(f):
			self.Paths[n] = f
		return tmp

	def Tempy(self, AnArg):
		return self.decor(AnArg)

aaa = temp()

@aaa.Tempy('test')
def SomeFunc(AMessage):
	print(AMessage*2)


aaa.Paths['test']('Heyy')