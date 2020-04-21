
# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!

# Import Libraries here:
from __future__ import print_function, unicode_literals
from colorama import Fore, Back, Style # type: ignore
from PyInquirer import prompt, print_json  # type: ignore
import threading
import json
import time
import random
import os
import playsound # type: ignore
from sys import platform

from colorama import init  # type: ignore
init()

# --------------------------
# |		Version!		|
# --------------------------
version = Style.DIM + Fore.WHITE + \
	"==> Development Version 0.3.6 \n" + Style.RESET_ALL
# --------------------------


# Define variables here:

# Used to prevent cheating:
devPassword = "hackerman"

mainLoop = 1
coins = 0  # fucking poor cunt lmao.
hp = 100
# Events used for random stuff:

progressDoor = True
events = ["store", "randomFight", "none", "bombTrap"]




# You deal more damage with the better sword you have, for example,
# having a stone sword deals 10% more damage then no sword.
# 0 = No Sword = 0% Extra damage
# 1 = Wooden Sword = 5% Extra damage
# 2 = Stone Sword = 10% Extra damage
# 3 = Iron Sword = 20% Extra damage
# 4 = Diamond Sword = 35% Extra damgage

# Armour absorbs a percentage of damage, for example having copper armour
# absorbs 10% damage, so if you get 50 damage, you only get 45

# 0 = No Armour = 1 x Damage taken
# 1 = Copper Armour = 0.9 x Damage taken
# 2 = Iron Armour = 0.8 x Damage taken
# 3 = Platinum Armour = 0.7 x Damage taken
# 4 = Diamond Armour = 0.6 x Damage taken



CSSOptions = [["Matches", 10], ["Basic Healing Potion", 20],
			  ["Copper Armour", 100], ["Stone Sword", 80]]

# 1 x Matches.
# 3 x Sticks.
# (no sword)
# No healing potions
# No Armour




success = Style.BRIGHT + Fore.GREEN + "==> "
rip = Style.BRIGHT + Fore.RED + "==> "
question = Style.BRIGHT + Fore.YELLOW + "[?] "
error = Style.BRIGHT + Fore.RED + "[!] "
hint = Style.DIM + Fore.WHITE + "(hint: "
action = Style.BRIGHT + Fore.YELLOW + "==> "
quote = Style.BRIGHT + Fore.WHITE + '"'



hasSeenAStore = False

# Define classes here:

# Some useful stuff

class Item:
	def init():
		self.amount=0
	def add(number):
		self.amount+=number
	def remove(number):
		self.amount-=number

class Inventory:
	matches = 1
	sticks = 3
	basicHealingPotion = 0


	sword = 0
	damage = 0


	armour = 0
	absorbtion = 0


class Scene:
	current = 1 # the current scene
	surroundingsLit = False
	hasStore = False
	hasCoins = False
	storeSelected = []
	# description of current room, called by observe and look around
	description = "You haven't started yet!"

# Define functions here:

def invalidCommand():
	print(error + "Invalid command! \n")


def useBrick():  # temp function called when in a specific room
	if Scene.current == 5:
		print(
			"you pull out the brick, however quickly drop it as a massive spider lay on it.")
		time.sleep(0.2)
		print("you hear a latch go *click!* and the sound of Bricks on Bricks filles the room... A massive door lays upon your sight.")
		progressDoor = True
	else:
		print("There are no bricks nearby...")


def passwordPrompt():
	print(Style.BRIGHT + Fore.YELLOW + "This is a developer command!"
		  " Please input the developer password!" + Style.RESET_ALL)
	questions = [
		{

			'type': 'password',
			'message': 'Enter the Developer password',
			'name': 'password'
		}
	]
	answers = prompt(questions)
	userInput = answers['password']
	if userInput == devPassword:
		print(success + "Access granted!\n" + Style.RESET_ALL)
		return "granted"
	else:
		print(rip + "Incorrect password!\n")
		return "denied"


def removeFromList(list, removal):
	index = 0
	listLoop = True
	while listLoop:
		if list[index] == removal:
			modifiedList = list
			modifiedList.pop(index)

			return modifiedList
			listLoop = False

		else:
			index = index + 1


def detect_system():
	global operatingsystem
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		operatingsystem = "unix"
	else:
		operatingsystem = "windows"


def clear():
	if operatingsystem == "unix":
		_ = os.system('clear')
	else:
		_ = os.system('cls')


def isDead():
	if hp < 0:
		gameover()


class soundThread (threading.Thread):
	def __init__(self, directory):
		threading.Thread.__init__(self, daemon=True)
		self.dir = directory


	def run(self):
		threadPlaySound(self.dir)


def threadPlaySound(path):
	playsound.playsound(path)


def playSound(path):
	theSoundThread = soundThread(path)
	theSoundThread.start()


def gameover():
	clear()
	print(rip + "Your body is torn into shreads...")
	time.sleep(2)
	print(Style.BRIGHT + Fore.YELLOW + ".")
	time.sleep(1)
	print("..")
	time.sleep(1)
	print("...\n")
	time.sleep(1)

	print(Style.BRIGHT + Fore.WHITE +

		  "   _____					   _\n"
		  " / ____|					  | |\n"
		  "| |  __  __ _ _ __ ___   ___	_____   _____ _ __| |\n"
		  "| | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__| |\n"
		  "| |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |  |_|\n"
		  " \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|  (_)\n"
		  )

	time.sleep(2)

	print(Style.BRIGHT + Fore.WHITE +
		  "Maybe next time, you might be a bit more lucky...\n")
	time.sleep(5)
	clear()
	exit()


def addCoins(add):
	global coins
	coins = coins + add
	print(success + ("You pocketed " + str(add) + " coins! \n"))


def removeCoins(value):
	global coins
	coins = coins - value
	print(rip + ("You dropped " + str(value) + " coins! \n"))


def spendCoins(value):
	global coins
	coins = coins + value
	print(success + ("You spent " + str(value) + " coins! \n"))


def ask(funcQuestion, answer1, answer2):
	askLoop = 1
	while askLoop == 1:
		# Asks the user a question
		userInput = input(question + "{funcQuestion} [{answer1}/{answer2}] "
						  .format(funcQuestion=funcQuestion, answer1=answer1, answer2=answer2)
						  + Style.RESET_ALL)

		# Checks if it's correct
		if userInput == answer1:
			askLoop = 0
			print("")
			return answer1
		elif userInput == answer2:
			askLoop = 0
			print("")
			return answer2
		else:
			print(error + "Answer must be either "
				  "{answer1} or {answer2}!\n".format(answer1=answer1, answer2=answer2))


def ask3(funcQuestion, answer1, answer2, answer3):
	askLoop = 1
	while askLoop == 1:
			# Asks the user a question
		userInput = input(question + "{funcQuestion} [{answer1}/{answer2}/{answer3}] "
						  .format(funcQuestion=funcQuestion, answer1=answer1, answer2=answer2, answer3=answer3)
						  + Style.RESET_ALL)

		# Checks if it's correct
		if userInput == answer1:
			askLoop = 0
			print("")
			return answer1
		elif userInput == answer2:
			askLoop = 0
			print("")
			return answer2
		elif userInput == answer3:
			askLoop = 0
			print("")
			return answer3

		else:
			print(error + "Answer must be either "
				  "{answer1}, {answer2} or {answer3}!\n".format(answer1=answer1,
																answer2=answer2, answer3=answer3))


def damage(value):
	global hp
	hp = hp - value
	print(rip + ("You lost " + str(value) + " health! \n"))
	isDead()


def heal(value):
	global hp
	hp = hp + value
	print(success + ("You gained " + str(value) + " health! \n"))
	if hp > 100:
		hp = 100


def combat(enemy, enemyHP, enemyMinDamage, enemyMaxDamage):
	global hp
	print(rip + "You get in a battle with {enemy}!\n".format(enemy=enemy))
	time.sleep(0.5)

	combatLoop = True
	while combatLoop:
		time.sleep(0.8)

		userInput = ask("Fight or Flee?", "fight", "flee")
		if userInput == "fight":
			# Calculates damage
			damage = random.randint(5, 10) * Inventory.damage
			enemyDamage = random.randint(
				enemyMinDamage, enemyMaxDamage) * absorbtion

			# Applies damage
			hp = hp - enemyDamage
			enemyHP = enemyHP - damage

			# Displays to user
			print(
				success + "You deal {damage} damage!".format(damage=round(damage)))
			print(
				rip + "{name} deals {damage} damage!\n".format(damage=round(enemyDamage), name=enemy))
			time.sleep(0.8)
			isDead()

			if enemyHP < 0:
				print(
					success + "You successfully killed {name}\n".format(name=enemy))
				time.sleep(0.8)
				extraCoins = random.randint(10, 25)
				addCoins(extraCoins)
				combatLoop = False
				return "kill"

		elif userInput == "flee":
			chance = random.randint(1, 2)
			if chance == 1:
				print(
					action + "You run away before {name} could catch you.\n".format(name=enemy))
				combatLoop = 0
				time.sleep(0.8)

				return "flee"

			elif chance == 2:
				print(
					action + "You tried to flee, but {name} caught you. \n".format(name=enemy))
				time.sleep(1)

				enemyDamage = random.randint(
					enemyMinDamage, enemyMaxDamage) * 2 * absorbtion
				hp = hp - enemyDamage
				print(rip + "{name} deals {damage} damage!\n"
					  .format(damage=round(enemyDamage), name=enemy))
				time.sleep(1)
				isDead()


# Commands used
def save_game():
	# NOTE: If you want to add your own variable, transferred
	# across saves, please add it in the saveFile place.

	print(hint + "For example, '/home/user/save.json')")
	directory = input(Style.RESET_ALL + question + "What is the file that you would "
					  "like to save in? ")

	saveFile = {
		"Inventory": {
			"Coins": coins,
			"Sticks": Inventory.sticks,
			"Matches": Inventory.matches,
			"Sword": Sword,
			"Armour": armour,
		},
		"other": {
			"damageMultiplyer": Inventory.damage,
			"absorbtion": absorbtion,
			"events": events,
			"Scene.current": Scene.current,
			"Scene.description": Scene.description,
			"surroundingsLit": surroundingsLit,
			"Scene.hasCoins": Scene.hasCoins,
		}
	}

	with open(directory, 'w', encoding='utf-8') as f:
		json.dump(saveFile, f, ensure_ascii=False, indent=4)

	print(success + "Successfully saved to {dir}!\n".format(dir=directory))


def load_game():
	# NOTE: If you want to add your own variable, transferred
	# across saves, please add it to the global and then...

	global coins
	global Sword
	global armour
	global Inventory
	global absorbtion
	global events
	global Scene
	global surroundingsLit

	directory = input(question + "What is the directory the save is in? ")

	with open(directory, 'r', encoding='utf-8') as f:
		saveFile = json.load(f)

	# ... add it here:
	coins = saveFile['Inventory']['Coins']
	Inventory.sticks = saveFile['Inventory']['Sticks']
	Inventory.matches = saveFile['Inventory']['Matches']
	Sword = saveFile['Inventory']['Sword']
	armour = saveFile['Inventory']['Armour']

	Inventory.damage = saveFile['other']['damageMultiplyer']
	absorbtion = saveFile['other']['absorbtion']
	events = saveFile['other']['events']
	Scene.current = saveFile['other']['Scene.current']
	Scene.description = saveFile['other']['Scene.description']
	surroundingsLit = saveFile['other']['surroundingsLit']
	Scene.hasCoins = saveFile['other']['Scene.hasCoins']

	print(success + "Successfully loaded save file!\n")


def checkCoins():
	global coins
	print(success + "You have $" + str(coins) + "!\n")
	if coins == 0:
		time.sleep(0.7)
		print(Style.BRIGHT + Fore.WHITE + "You have 0 coins? I feel bad, here"
			  " take 10 coins!")
		time.sleep(0.7)
		addCoins(10)
		time.sleep(0.7)


def openInventory():
	print(success + "Inventory:")
	count = 0
	if Inventory.matches != 0:
		print(str(Inventory.matches) + " x Matches")

	if Inventory.sticks != 0:
		print(str(Inventory.sticks) + " x Sticks")

	if Inventory.basicHealingPotion != 0:
		print(str(Inventory.basicHealingPotion) + " x Basic Healing Potion")

	if Inventory.sword == 1:
		print("Wooden Sword")
	elif Inventory.sword == 2:
		print("Stone Sword")

	if Inventory.armour == 1:
		print("Copper Armour")

	# This print just adds some white space
	print(" ")


def purchase(storeSelected, id):
	global coins
	global absorbtion
	global damageMultiplyer
	global basicHealingPotion

	item = storeSelected[id][0]
	price = storeSelected[id][1]
	if coins >= price:
		if item == "Matches":
			Inventory.matches = Inventory.matches + 1
		elif item == "Basic Healing Potion":
			Inventory.basicHealingPotion = Inventory.basicHealingPotion + 1
		elif item == "Copper Armour":
			if Inventory.armour == 1:
				print(error + "You already have this item!\n")
				return "bruh"
			else:
				Inventory.armour = 1
				Inventory.absorbtion = 0.9
		elif item == "Stone Sword":
			if Inventory.sword == 2:
				print(error + "You already have this item!\n")
				return "bruh"
			else:
				Inventory.sword = 2
				Inventory.damage = 1.1

		print(action + "You purchased {item} for {price} coins!\n"
			  .format(item=item, price=price))
		coins = coins - price
	else:
		print(error + "You do not have enough coins to purchase this item!\n")


def openStore():
	global CSSOptions
	global Inventory
	global coins
	print("------------------")
	print("	  STORE	   ")
	print("------------------")
	print(success + "You have $", str(coins))
	for i in Scene.storeSelected:
		print(Fore.WHITE + "{name} -- {price}".format(name=i[0], price=i[1]))
	print("")

	questions = [
		{
			'type': 'list',
			'name': 'itemChoice',
					'choices': [(Scene.storeSelected[0])[0],
								(Scene.storeSelected[1])[0],
								(Scene.storeSelected[2])[0], 'Exit'],
			'message': 'Which item would you like to purchase?',
		}
	]

	askLoop = 1
	while askLoop == 1:
		answers = prompt(questions)
		# print_json(answers)
		userInput = answers['itemChoice']
		# print(action + "You selected:" + userInput)
		if userInput == "Exit":
			askLoop = 0
			print(action + "You left the store.\n")

		elif userInput == Scene.storeSelected[0][0]:
			purchase(Scene.storeSelected, 0)

		elif userInput == Scene.storeSelected[1][0]:
			purchase(Scene.storeSelected, 1)

		elif userInput == Scene.storeSelected[2][0]:
			purchase(Scene.storeSelected, 2)


def useMatch():
	global Inventory
	global surroundingsLit
	global Scene

	if Inventory.matches == 0:
		print(error + "You don't have any matches!\n")
	elif Scene.surroundingsLit == True:
		Inventory.matches = Inventory.matches - 1
		print("You light a match. it begins to burn away.")
		print(rip + "You used up one match. \n")

	elif Scene.surroundingsLit == False:
		Scene.description = "This place is in ruins, and it's possibly been like that for decades."
		Inventory.matches = Inventory.matches - 1
		Scene.surroundingsLit = True
		print("You Light a match, your surroundings fill up with light. "
			  "you can now see!")
		print(rip + "You used up one match. \n")


def start():
	global Scene
	global progressDoor

	Scene.storeSelected = []
	initStore()

	if Scene.surroundingsLit == False:
		print("You find yourself in an odd and dark place... \nWhat could this"
			  " possibly be?\n")
		Scene.description = "This place is extremely dark, you can't see anything..."
		time.sleep(1)

		print(
			"Check your Inventory, you might have something to \nimprove your vision...\n")
		time.sleep(1)
		# combat("Bob", 69)
		# print("Maybe I should use a match to light this place up...") # too straight forward.

		# print(hint + "type 'm' to use a match)\n" + Style.RESET_ALL) # too straight forward.
	else:
		if Scene.current == 1:
			# NOTE: describe this 'place'!
			print("This place looks like it's been abandoned decades ago...")
			# NOTE: describe this 'creature'! e.g. this oddly hunched over creature
			print(action + "An odd creature begins to walk up to you... \n")
			answer = ask("Should you hide or confront them?", "h", "c")
			if answer == "c":
				# User selected confront
				# Nothing special happens, it is passed on to the next part
				pass

			elif answer == "h":
				# User selected hide
				print(action + "You tried to hide, but there was nowhere to go, "
					  "the figure began to confront you.")
				time.sleep(1.5)

			print(action + "The odd figure got close enough until you "
				  "could see it.")  # NOTE: so is this a creature or figure
			time.sleep(1)

			print(action + "The figure looked like an ancient wizard. \n")
			time.sleep(1)

			input(quote + 'Greetings, it seems you are new here,'
				  ' is that true?"\n' + Style.RESET_ALL)

			# NOTE: maybe. give the user a choice to say something.
			print(action + "You said yes. \n")
			time.sleep(0.7)

			print(quote + "I see, this is a dangerous place, so tread"
				  ' carefully..."')  # ITS DANGEROUS TO GO ALONE.
			time.sleep(1)

			print(quote + 'Here, take this, it will help you defend yourself."')
			time.sleep(2)  # TAKE THIS.

			print(success + "You recieved a basic Sword.")
			print(success + "You recieved a basic Healing Potion.")
			addCoins(50)

			global Inventory

			Inventory.basicHealingPotion = Inventory.basicHealingPotion + 1
			Inventory.damage = 1.05
			Inventory.sword = 1
			Scene.current = 2
			time.sleep(2)
			start()

		elif Scene.current == 2:
			print(action + "You ask the ancient wizard:")
			time.sleep(1)

			print(Style.RESET_ALL + "Who are you?")
			time.sleep(1)
			print("What is this place? \n")
			time.sleep(1)

			print(action + "The wizard responds \n")
			time.sleep(1.5)

			print(quote + 'This place is an underground town, it used to be'
				  ' thriving, there were plenty of stores, lots of jobs, it was'
				  ' a great place to be...\n But then, the rebellion came in'
				  ' and wiped this place out, everybody either escaped or died.\n'
				  ' And me, I was the founder of this town." \n')
			time.sleep(8)
			Scene.description = "This place is in ruins, apparently it's supposed to be a town...\nThere is a door to the next room, something seems to be strung across it."

			input(quote + 'Would you like to recieve a quest?" \n'
				  + Style.RESET_ALL)
			print(action + "You said yes. \n")
			time.sleep(0.8)

			print(quote + 'Try and recover the Great Stone of Knowledge,'
				  ' it is located in the north-east room, however it is guarded'
				  ' by very powerful Almogates." \n')
			time.sleep(3)

			print(quote + 'Good luck." \n')
			playSound("Music/federation.mp3")
			print(hint + "This song isn't mine and I don't own any rights to it.)")
			print(hint + "Ben Prunty made this song, it's called 'Federation'.)")
			print(hint + "I will remove this later when I get another song.)" + Style.RESET_ALL)
			time.sleep(1)

			print(action + "He leaves the room and now, you're on your own. \n")
			Scene.current = 3

		elif Scene.current == 3:
			Scene.description = "The room looked very charred after the explosion. you should probably proceed."

			print(action + "After the wizard left, you went into the next room. \n")
			time.sleep(1.5)

			print(action + "It is odly quiet here... you begin to look around... \n")
			time.sleep(2)

			playSound("Sounds/explosion.wav")
			print(rip + "BANG!")
			time.sleep(0.2)
			print("  A small bomb exploded, it was a trap!")
			damage(20)
			time.sleep(1)
			Scene.current = 4

		elif Scene.current == 4:
			print(
				action + "You proceed to the next room, being very careful where you step.")

			Scene.description = "This room is rather empty, but an old and dried up fountain lays ahead.\nA few coins lay scattered across the bottom, maybe you can pick them up? But however a single loose red brick in the wall north to you catches your eye..."
			progressDoor = False

			Scene.hasCoins = True
			time.sleep(1)

			print(action + "You quickly hear a movement and freeze...\n")
			time.sleep(1)

			print(quote + 'IT WAS YOU WHO DID IT! Y-YOU WERE THE ONE WHO KILLED ALL M'
				  '-MY F-F-FRIENDS!"\n')
			time.sleep(1.5)
			print(action + "You try to explain that they were mistaken but"
				  " it was too late. \n")
			time.sleep(1)

			theResult = combat("Unidentified", 25, 5, 10)
			if theResult == "kill":
				print(
					action + "You killed the unknown person however, you can't stop feeling bad. \n")

			elif theResult == "flee":
				print(action + "You quickly ran away, you're safe now. \n")

			Scene.current = 5

		elif Scene.current == 5:
			print("whew! thats over!")


def hpCheck():
	# Displays different colour depending on hp
	global hp
	if hp > 100:
		hp = 100

	hp = round(hp)

	if hp > 70:
		print(
			success + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))

	elif hp > 35:
		print(
			action + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))

	else:
		print(rip + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))


def randomEvent():
	print("This is a randomly generated event! The stories in here have not been completed yet.")

	global events
	global hasSeenAStore
	global Scene
	global storeSelected
	randomLoop = True

	if len(events) > 0:
		selection = random.choice(events)
		if selection == "store":
			Scene.description = Scene.description + \
				" There is a store nearby, they might sell something useful..."
			if hasSeenAStore == False:
				print(hint + "There is a store in this room! you can buy items from them, however you might have to \"look around\" to find it!")
			storeOptions = CSSOptions.copy()

			Scene.hasStore = True

		elif selection == "randomFight":
			randomEnemy()

		elif selection == "none":
			print("")
		elif selection == "bombTrap":
			playSound("Sounds/explosion.wav")
			print(rip + "BANG!")
			time.sleep(0.2)
			print("  A small bomb exploded, it was a trap!")
			damage(20)
			Scene.description = Scene.description + " The room looked very charred after the explosion."
		elif selection == "wizardThatWantsToKillYou":
			print(quote + 'You. You have the information you need.\n'
				  '')
			pass

		events = removeFromList(events, selection)

	else:
		print("There are no more unvisited events left!")


def initStore():
	global Scene
	storeOptions = CSSOptions.copy()
	i = 0
	while i < 3:
		i += 1
		theChosenOne = random.choice(storeOptions)

		Scene.storeSelected.append(theChosenOne)
		storeOptions = removeFromList(storeOptions, theChosenOne)


class Enemy:
	def __init__(self, name, health, minDamage, maxDamage):
		self.health = health
		self.name = name
		self.minDamage = minDamage
		self.maxDamage = maxDamage

	def __del__(self):
		print("%s has died" % (self.name))

	def takeDamage(self, damage):
		self.health -= damage
		if (self.health <= 0):
			self.die()

	def die(self):
		del self

	def startBattle():
		combat(self.name, self.health, self.minDamage, self.maxDamage)



def randomEnemy():
	# [Name, Health, Enemy Minimum Damage, Enemy Maximum Damage]
	# enemyName, enemyHealth, enemyMinDamage, enemyMaxDamage
	# names = [["Unidentified", 25, 5, 10], ["Wizard", 40, 10, 20],
	#		 ["Giant Spider", 25, 5, 15], ["Bob", 100, 1, 1]]

	enemies = [Enemy("Unidentified", 25, 5, 10), Enemy("Wizard", 40, 10, 20)]

	enemy = random.choice(enemies)
	enemy.startBattle()
	#combat(decision[0], decision[1], decision[2], decision[3])


def lookAround():
	print(Scene.description + "\n")


def pickCoins():
	global Scene

	if Scene.hasCoins == True:
		amount = random.randint(4, 6)
		print(action + "You reach out and grab all the coins")
		time.sleep(0.8)

		addCoins(amount)
		Scene.hasCoins = False

	else:
		print(error + "There are no coins to pick up! \n")


def healingPotion():
	if Inventory.basicHealingPotion > 0:
		askLoop = 1
		print(success + "[1] You have {amount} basic healing potions\n"
			  .format(amount=Inventory.basicHealingPotion))

		while askLoop:
			userInput = input(
				question + "Which potion would you like to use? ")
			if userInput == "1":
				# Displays to user
				print("You have selected the basic healing potion\n")
				time.sleep(0.8)
				print(rip + "You used up 1 basic healing potion")
				# Applies the changes
				heal(20)
				time.sleep(0.8)
				Inventory.basicHealingPotion = Inventory.basicHealingPotion - 1
				askLoop = 0
			else:
				print(error + "Answer must be either 1, 1 or 1!\n")
	else:
		print(error + "You don't have any potions!\n")


def main():
	detect_system()

	command = input(Style.BRIGHT + Fore.CYAN + "[Action] " + Style.RESET_ALL)
	if command in ("check money", "check coins", "coins", "money", "c"):
		checkCoins()

	elif command in ("open inventory", "open inv", "inventory", "inv", "i", "check inventory", "check inv"):
		openInventory()

	elif command in ("use match", "strike match", "match", "light match",
					 "use matches", "matches", "m"):
		useMatch()

	elif command in ("h", "help", "umm", "asdfghjkl", "qwertyuiop"):
		print("Help menu \n")

	elif command in ("e", "exit", "close", "alt-f4"):
		global mainLoop
		mainLoop = 0

	elif command in ("hp", "health", "health points"):
		hpCheck()
	elif command in ("goto shop", "goto store", "store", "shop"):
		print("You entered the store!")
		openStore()
	elif command in ("s", "start", "next", "proceed", "next room", "forth", "enter door", "go through door"):
		if progressDoor == True:
			Scene.hasStore = False

			start()
		else:
			print("Progress through where? there are no visible exits!\n")

	elif command in ("l", "look around", "look", "observe"):
		lookAround()
	elif command in ("pickup loose brick", "use loose brick", "use brick", "pickup brick", "brick"):
		useBrick()
	elif command in ("cl_event", "plsevent"):
		# NOTE: This is for only debugging!
		if passwordPrompt() == "granted":
			randomEvent()

	elif command in ("cl_battle", "plsbattle"):
		# NOTE: This is for only debugging!
		if passwordPrompt() == "granted":
			randomEnemy()

	elif command in ("version", "ver"):
		print(version)

	elif command in ("pickup coins", "pick up coins", "pick coins"):
		pickCoins()

	elif command in ("heal", "potion"):
		healingPotion()

	elif command in ("cl_store", "plsstore"):
		# NOTE: This is for only debugging!
		if passwordPrompt() == "granted":
			openStore()

	elif command in ("cl_rich", "cl_addcoins", "plscoins"):
		print("The money grinch steps out of the shadows\n")
		time.sleep(1)
		print(quote + "In need of coins, eh? I mean i could let you have some of my precious coins, but ya gotta know the secret code.\"")
		print(" he said grouchingly\n")
		time.sleep(2)
		print(quote + "Go ahead. I'm waiting...\n")
		time.sleep(1)

		if passwordPrompt() == "granted":
			addCoins(200)

	elif command in ("save", "save game"):
		save_game()

	elif command in ("load", "load game"):
		load_game()

	else:
		invalidCommand()


detect_system()
clear()

# Introduce the user:
print(Style.BRIGHT + "Welcome to " + Fore.BLUE + "DungeonCli!" + Style.RESET_ALL)

print(version)
print(Style.RESET_ALL + "Type 'h' for help or 's' to start! \n")

# Run those functions here:
initStore()
while mainLoop == 1:
	main()

# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# https://www.youtube.com/watch?v=GGmuA7PK-cc
