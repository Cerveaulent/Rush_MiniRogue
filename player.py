from random import randint
from monster import MonsterTypeA

class Player():
	def __init__(self):
		self.health = 12
		self.att_damage = 3
		self.x = 3
		self.y = 3

	def get_hit(self, monster, win, height, width):
		win.addstr(height - 2, width - 39, "You got hit by {} and lost {} health".format(monster.name, \
			monster.att_damage))
		self.health -= monster.att_damage

	def attack(self, monster, win, height, width):
		if randint(0, 1) :
			win.addstr(height - 2, 0, "You hit and dealt {} damage to {}".format(self.att_damage, \
				monster.name))
			monster.get_hit(self)
		else :
			win.addstr(height - 2, 0, "You missed {}".format(monster.name))