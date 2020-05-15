from random import randint

class Monster(object):
	"""docstring for Monster"""
	def __init__(self, pos_x, pos_y, room):
		self.name = ""
		self.health = 0
		self.att_damage = 0
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.room = room
		pass
	def get_hit(self, player):
		self.health -= player.att_damage

	def attack(self, player, win, height, width):
		if randint(0, 1) :
			player.get_hit(self, win, height, width)
		else :
			win.addstr(height - 2, width - 39, "                      {} missed you".format(self.name))		
		

class	MonsterTypeA(Monster):
	def __init__(self, pos_x, pos_y, room):
		super(MonsterTypeA, self).__init__(pos_x, pos_y, room)
		self.name = "Statue"
		self.health = 5
		self.att_damage = 1
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.room = room

	def moveset(self, r_width, r_height):
		rand_num = randint(1, 5)
		if  rand_num == 1 :
			self.pos_x -= 1
		elif rand_num == 2 :
			self.pos_x += 1
		elif rand_num == 3 :
			self.pos_y -= 1
		elif rand_num == 4 :
			self.pos_y += 1
		elif rand_num == 5 :
			pass

class MonsterTypeB():
	def __init__(self):
		self.name = "typeB"
		self.health = 9
		self.att_damage = 1
		
class MonsterTypeS():
	def __init__(self):
		self.name = "typeS"
		self.health = 1
		self.att_damage = 1