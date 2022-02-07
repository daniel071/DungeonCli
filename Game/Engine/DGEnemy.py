from . import DGCombat
class Enemy:
	def __init__(self, name, health, minDamage, maxDamage):
		self.health = health
		self.name = name
		self.minDamage = minDamage
		self.maxDamage = maxDamage

	def takeDamage(self, damage):
		self.health -= damage
		if (self.health <= 0):
			self.die()

	def die(self):
		del self

	def startBattle(self):
		DGCombat.combat(self.name, self.health, self.minDamage, self.maxDamage)

	def upgrade():
		print("todo")
		#save this for upgrading the enemies difficulty later in the game