class Room():
	def __init__(self, height, width):
		self.width = width
		self.height = height

class	Treasure():
	def __init__(self, pos_x, pos_y, room, symbol):
		self.name = ""
		self.symbol = symbol
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.room = room

class	Arrivee():
	def	__init__(self, pos, pos_x, pos_y):
		self.room = pos
		self.pos_x = pos_x
		self.pos_y = pos_y