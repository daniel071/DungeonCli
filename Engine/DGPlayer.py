# This holds the Inventory of the player
coins = 0  # fucking poor cunt lmao.
hp = 100


class Inventory:
	# You deal more damage with the better sword you have, for example,
	# having a stone sword deals 40% more damage then no sword.
	# 0 = No Sword = 0% Extra damage
	# 1 = Wooden Sword = 20% Extra damage
	# 2 = Stone Sword = 40% Extra damage
	# 3 = Iron Sword = 70% Extra damage
	# 4 = Diamond Sword = 100% Extra damage

	# Armour absorbs a percentage of damage, for example having copper armour
	# absorbs 20% damage, so if you get 50 damage, you only get 40

	# 0 = No Armour = 1 x Damage taken
	# 1 = Copper Armour = 0.8 x Damage taken
	# 2 = Iron Armour = 0.6 x Damage taken
	# 3 = Platinum Armour = 0.4 x Damage taken
	# 4 = Diamond Armour = 0.2 x Damage taken


	# 1 x Matches.
	# 3 x Sticks.
	# (no sword)
	# No healing potions
	# No Armour


	# You can spend coins on a coins multiplyer which will
	# multiply the amount of coins you get!
	moneyMultiplyer = 1.0

	# TODO: Add a evasian multiplyer!
	# This will increase the change your enemy will miss!

	matches = 1
	sticks = 3

	# Basic healing potion heals 20 health
	basicHealingPotion = 0

	# Advanced healing potion heals 50 health
	advancedHealingPotion = 0

	# Posion potion deals (a lot of damage) * Damage multiplyer
	poisonPotion = 0

	sword = 0
	damage = 1.0

	armour = 0
	absorbtion = 1.0
