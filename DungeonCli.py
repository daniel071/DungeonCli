# NOTE: JOIN THE DISCORD: https://discord.gg/eAUqKKe

# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!

# Import Libraries here:
#from __future__ import print_function, unicode_literals
#from __future__ import print_function
from colorama import Fore, Back, Style# type: ignore
from PyInquirer import prompt, print_json # type: ignore
import threading
import json
import time
import random
import os
import sys
import simpleaudio
from Engine import *
try:
   from src import richPrecense
except:
    print("warning: missing package? or discord isn't running...")
from src import multiplayer
from simpleaudio import _simpleaudio
from pydub import generators
from pydub.playback import _play_with_simpleaudio
import pydub
from sys import stdout
# from defKey import defKey
from threading import Lock
# import multiprocessing # DANIEL YOU CUNK :) PLS USE THREADS!!
					   # ONCE I FIGURE OUT HOW TO END THREADS, XENTHIO!
					   # You know how hard it is?
					   # YES I NEEDED TO DO THE SAME THING! BUT YOU KNOW THREADS END AFTER THE FUNCTION FINISHES, RIGHT?
					   # I CAN'T MAKE A BUILD UNTIL YOU SWITCH TO THREADS...
					   # I KNOW THAT A THREAD ENDS WHEN THE FUNCTION END,
					   # BUT I CAN'T END A PLAYSOUND() FUNCTION UNTIL IT FINISHES
					   # ALSO WHY ARE WE TALKING IN CAPS LOCK?
					   # AND WHY ARE WE USING THIS TO CHAT? Lol.
					   # IDK BUT KEEP THIS GIANT BLOCK OF TEXT FOR HISTORICAL PURPOSES, OR ATLEAST UNTIL YOU USE THREADS.


from colorama import init  # type: ignore

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --------------------------
# |		Version!		|
# --------------------------
version = "Development Version 0.5.14"
# --------------------------

DGText.printScan("ok")
# Define variables here:

all_processes = []
combatOverrideMusic = True

# Used to prevent cheating:
devPassword = "hackerman"
developer = 0

playMusic = True
invalidCommands = 0
mainLoop = 1
coins = 0  # fucking poor cunt lmao.
hp = 100
# Events used for random stuff:

# TODO: when 'wizardThatWantsToKillYou' is done, add it here
events = ["store", "store", "store", "randomFight", "none", "none", "none", "bombTrap",
"treasure", "treasure"]

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



CSSOptions = [["Matches", 5], ["Basic Healing Potion", 15],
			  ["Copper Armour", 75], ["Iron Armour", 125], ["Stone Sword", 60],
			  ["Iron Sword", 90],
			  ["Advanced Healing Potion", 60], ["Poison Potion", 20]]

battleSongs = ["Music/Ambient_fight_1.ogg", "Music/interstellar_space_dryer_2.ogg"]

# 1 x Matches.
# 3 x Sticks.
# (no sword)
# No healing potions
# No Armour




# theCombatHasNotFinished! alsoICanTalkInCamelCaseMakesSenseRight?
hasCombatFinished = "no."
hasSeenAStore = False

# Define classes here:

# Some useful stuff




Scene = DGScene





class quest:
	quests = []

	def add(newQuest):
		quest.quests.append(newQuest)

	def list():
		DGText.printScan(DGText.success + "Your current quests:")
		for theQuest in quest.quests:
			DGText.printScan(Style.BRIGHT + Fore.CYAN + theQuest)

		print(Style.RESET_ALL)



class randomDialog:
	def bombExplodes(self):
		dialog=["A small bomb exploded, it was a trap!\n",
		"Ouch! You tripped a small Bomb trap!\n",
		"You attempted to avoid the obvious trap, however it set off a small bomb!\n"]

		return random.choice(dialog)


	def collectCoins(self):
		dialog=["You reach out and grab all the coins.",
		"You stuff your pockets with the coins.",
		"You reach out in awe to consieve all the coins."]
		return random.choice(dialog)


	def gameoverText(self):
		dialog=["Maybe next time, you might be a bit more lucky...\n",
		"Maybe next time, things might be in your favour...\n",
		"Maybe next time, you'll be more careful...\n",
		"Maybe next time, you might not be where you are now...\n",
		"Maybe next time, you'll be more wise...\n",
		"Maybe next time, you'll choose the right option...\n",
		"Maybe next time, you won't be so careless...\n",
		"Maybe next time, things might actually go right...\n",
		"Maybe next time, you'll remember that you are mortal...\n"]
		return random.choice(dialog)

	def roomDescription(self):
		dialog=["The ceiling in this room hangs really low. Seeing it is truly a strange sight.",
		"It's oddly ambient in here, water trickles down the walls. It's rather relaxing.",
		"This room is massive."]
		return random.choice(dialog)

	def coinsOnFloor(self):
		dialog=["There are some coins on the floor.",
		"Some coins are scattered on the ground.",
		"There are some coins nearby."]
		return random.choice(dialog)
	def store(self):
		dialog=["There is a store in this room.",
		"And old store is setup in here..",
		"An old shack with the letters \'Store\' is nearby."]
		return random.choice(dialog)
printspeed = 0.013
defprntspd = 0.013

def initRandomRoom():
	# Not my code but what I think it does is
	# has a 50% chance of placing coins in the room.
	# Also, there would be a 1 in 10 chance of the room not being lit
	global Scene
	a = random.randint(1,2)
	Scene.description = randomDialog.roomDescription(randomDialog)
	if a == 2:
		Scene.hasCoins == True
		Scene.description == Scene.description + " " + randomDialog.coinsOnFloor(randomDialog)
	b = random.randint(1,10)
	if b == 2:
		Scene.surroundingsLit == False








# class inputDetector:
# 	def __init__(self):
# 		self._running = True
#
# 	def terminate(self):
# 		self._running = False
#
# 	def run(self, n):
# 		while self._running and n > 0:
# 			global printspeed
# 			if kbhit() == true:
# 				printspeed = 0.00001
# Define functions here:






def invalidCommand():
	global invalidCommands

	invalidCommands = invalidCommands + 1
	DGText.printScan(DGText.error + "Invalid command! \n")
	if invalidCommands > 3:
		DGText.printScan(hint + "if you're stuck on how to progress, simply type 's')\n"
		+ Style.RESET_ALL)
		invalidCommands = 0


def useBrick():  # temp function called when in a specific room
	global Scene
	if Scene.current == 8:
		DGText.printScan(action + "You pull out the brick however, quickly drop it as a massive spider lay on it.")
		time.sleep(0.7)
		DGText.printScan("You hear a latch go *click!* and the sound of Bricks on Bricks"
		" fill the room... A massive door lays upon your sight.\n")
		time.sleep(1)

		Scene.description = "A massive door is upon your sight. You should probably check it out"
		Scene.canProgress = True
	else:
		DGText.printScan(error + "There are no bricks nearby!\n")


def passwordPrompt():
	if developer == 0:
		DGText.printScan(Style.BRIGHT + Fore.YELLOW + "This is a developer command!"
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
			DGText.printScan(DGText.success + "Access granted!\n" + Style.RESET_ALL)
			return "granted"
		else:
			DGText.printScan(rip + "Incorrect password!\n")
			return "denied"
	else:
		DGText.printScan(DGText.success + "you have already use the dev password, so you're still logged in.")
		return "granted"


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


def isDead():
	if hp < 0:
		gameover()


def playSound(path, ifLoop):
	global all_process
	if playMusic == True:
		if ifLoop is True:
			playback = _play_with_simpleaudio(pydub.AudioSegment.from_ogg(path) * 20)
		else:
			playback = _play_with_simpleaudio(pydub.AudioSegment.from_ogg(path))

		all_processes.append(playback)
	else:
		return "No music played"


def gameover():
	endThreads()
	playSound("Music/gameOver.ogg", False)
	DGMain.DGClear()
	DGText.printScan(rip + "Your body is torn into shreads...")
	time.sleep(2)
	DGText.printScan(Style.BRIGHT + Fore.YELLOW + ".")
	time.sleep(1)
	DGText.printScan("..")
	time.sleep(1)
	DGText.printScan("...\n")
	time.sleep(1)

	DGText.printScan(Style.BRIGHT + Fore.WHITE +

		  "   _____					   _\n"
		  " / ____|					  | |\n"
		  "| |  __  __ _ _ __ ___   ___	_____   _____ _ __| |\n"
		  "| | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__| |\n"
		  "| |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |  |_|\n"
		  " \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|  (_)\n"
		  )

	time.sleep(2)

	DGText.printScan(Style.BRIGHT + Fore.WHITE +
		  randomDialog.gameoverText(randomDialog))
	time.sleep(4)
	DGClear()
	endThreads()
	sys.exit()


def addCoins(add):
	global coins
	coins = coins + add
	DGText.printScan(DGText.success + ("You pocketed " + str(add) + " coins! \n"))


def removeCoins(value):
	global coins
	coins = coins - value
	DGText.printScan(rip + ("You dropped " + str(value) + " coins! \n"))


def spendCoins(value):
	global coins
	coins = coins + value
	DGText.printScan(DGText.success + ("You spent " + str(value) + " coins! \n"))


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
			DGText.printScan("")
			return answer1
		elif userInput == answer2:
			askLoop = 0
			DGText.printScan("")
			return answer2
		else:
			DGText.printScan(error + "Answer must be either "
				  "{answer1} or {answer2}!\n".format(answer1=answer1, answer2=answer2))


def damage(value):
	global hp
	hp = hp - value
	DGText.printScan(rip + ("You lost " + str(round(value)) + " health! \n"))
	isDead()


def heal(value):
	global hp
	hp = hp + value
	DGText.printScan(DGText.success + ("You gained " + str(value) + " health! \n"))
	if hp > 100:
		hp = 100


def bombTrapScene():
	global Scene

	Scene.description = "The room looked very charred after the explosion. you should probably proceed."

	DGText.printScan(action + "It is odly quiet here... you begin to look around... \n")
	time.sleep(2)

	playSound("Sounds/explosion.ogg", False)
	DGText.printScan(rip + "BANG!")
	time.sleep(1)
	DGText.printScan(randomDialog.bombExplodes(randomDialog))
	damage(random.randint(5, 15) * Inventory.absorbtion)
	time.sleep(1)



def combat(enemy, enemyHP, enemyMinDamage, enemyMaxDamage):
	global hp
	global Inventory
	global combatEnemyHP
	global hasCombatFinished

	hasCombatFinished = "no."


	def finishUpMusic():
		endThreads()
		playSound("Music/quest.ogg", True)



	def enemyDealDamage(multiplyer):
		global hp
		isMiss = random.randint(1,6)
		if isMiss == 5:
			DGText.printScan(action + "{name} missed!".format(name=enemy))
			DGText.printScan(DGText.success + "You took no damage!\n")
		else:
			enemyDamage = random.randint(enemyMinDamage, enemyMaxDamage) * Inventory.absorbtion * multiplyer
			hp = hp - enemyDamage

			DGText.printScan(rip + "{name} deals {damage} damage!"
			.format(damage=round(enemyDamage), name=enemy))
			time.sleep(0.4)
			if hp < 0:
				combatLoop == False

			isDead()


	def playerDealDamage(enemyHP):
		# for some reason this function couldn't use enemyhp???? so I made
		# a seperate one so it would work... :)

		global hasCombatFinished
		global hp
		global combatLoop
		global inventory

		isMiss = random.randint(1,7)
		isCritical = random.randint(1, 5)
		if isMiss == 1:
			DGText.printScan(action + "You missed!")
			DGText.printScan(rip + "You dealt no damage!")


		else:
			playerDamage = random.randint(5, 10)
			playerDamage = playerDamage * Inventory.damage
			enemyHP = enemyHP - playerDamage

			if isCritical == 1:
				DGText.printScan(DGText.success + "Critical hit!")
				DGText.printScan(DGText.success + "You deal double damage!\n")
				playerDamage = playerDamage * 2

			DGText.printScan(DGText.success + "You deal {damage} damage!".format(damage=round(playerDamage)))
			time.sleep(0.2)

			if enemyHP < 0:
				combatLoop = False
				DGText.printScan(DGText.success + "You DGText.successfully killed {name}\n"
				.format(name=enemy))

				time.sleep(0.4)

				extraCoins = random.randint(25, 35)
				addCoins(extraCoins)

				combatLoop = False

				finishUpMusic()

				hasCombatFinished = "killed"

		if combatOverrideMusic == False:
			regenerated = random.randint(1000, 2000)
			enemyHP = enemyHP + regenerated
			DGText.printScan(rip + "The boss regenerated {amount} hp!".format(amount=regenerated))

		return enemyHP


	if combatOverrideMusic == True:
		endThreads()
		songToPlay = random.choice(battleSongs)
		playSound(songToPlay, True)

	global hp
	DGText.printScan(rip + "You get in a battle with {enemy}!\n".format(enemy=enemy) + Style.RESET_ALL)
	time.sleep(0.5)

	questions = [
		{
			'type': 'list',
			'name': 'userChoice',
					'choices': ['Fight',
								'Flee',
								'Use item',
								'Check HP'],
			'message': 'What would you like to do?',
		}
	]

	combatLoop = True
	while combatLoop:
		if hasCombatFinished == "killed":
			combatLoop = False
			return "killed"


		print(Style.RESET_ALL)
		answers = prompt(questions)
		userInput = answers['userChoice']
		if userInput == "Fight":
			enemyDealDamage(1)
			enemyHP = playerDealDamage(enemyHP)


		elif userInput == "Flee":
			attemptFlee = random.randint(1, 2)
			if attemptFlee == 1:
				DGText.printScan(action + "You tried to flee, but {name} caught you. \n"
				.format(name=enemy))
				enemyDealDamage(1.5)

			else:
				DGText.printScan(action + "You run away before {name} could catch you.\n"
				.format(name=enemy))
				combatLoop = False
				time.sleep(0.4)

				finishUpMusic()

				return "flee"

		elif userInput == "Use item":
			potionQuestion = [
				{
					'type': 'list',
					'name': 'userChoice',
							'choices': ['Healing Potion',
										'Poison Potion',],
					'message': 'What potion type would you like to use?',
				}
			]

			theAnswer = prompt(potionQuestion)
			theEpicOption = theAnswer['userChoice']

			if theEpicOption == "Healing Potion":
				theOutput = healingPotion()
				if theOutput != "notUsed":
					if theOutput != 0:
						i = 0
						while i < theOutput:
							enemyDealDamage(1)
							i = i + 1


			elif theEpicOption == "Poison Potion":
				theOutput = usePoisonPotion()
				if theOutput != 0:
					# Saves current damage, multiplies it by 3 then sets it back.
					originalDamage = Inventory.damage
					Inventory.damage = Inventory.damage * 3
					playerDealDamage(enemyHP)
					Inventory.damage = originalDamage


		elif userInput == "Check HP":
			hpCheck()
			DGText.printScan(action + "The enemy has {amount} hp!\n".format(amount=round(enemyHP)))
			time.sleep(0.2)

		print("")

# Commands used
def bossBattle():
	global combatOverrideMusic
	global defprntspd
	endThreads()
	DGClear()

	defprntspd = 0.05

	DGText.printScan(action + "The door behind you closes. There is no escape.")
	time.sleep(2)
	DGText.printScan(quote + "I've been expecting you. Any last words?\"\n")
	time.sleep(2)
	DGText.printScan(quote + "Nothing eh? You're too weak to defeat me,"
	" and there's nothing that can stop me.\"\n")

	playSound("Music/bossBattle.ogg", True)

	defprntspd = 0.7
	print(Style.BRIGHT + Fore.WHITE)
	DGText.printScan("\"goodbye.\"\n")
	defprntspd = 0.013

	combatOverrideMusic = False
	bossLoop = True
	while bossLoop == True:
		theResult = combat("Boss", 25000, 1000, 1500)
		if theResult == "killed":
			bossSuccess()

		elif theResult == "flee":
			DGText.printScan(quote + "You think you can run away from me?\"")
			time.sleep(1)
			DGText.printScan(quote + "Think again.\"")
			time.sleep(1)

		endThreads()
		playSound("Music/bossBattle.ogg", True)


def bossSuccess():
	global defprntspd

	endThreads()
	DGClear()
	playSound("Music/endCredits.ogg", False)

	message = """
	__   __                     _       _
	\ \ / /__  _   _  __      _(_)_ __ | |
	 \ V / _ \| | | | \ \ /\ / / | '_ \| |
	  | | (_) | |_| |  \ V  V /| | | | |_|
	  |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)
	"""
	DGText.printScan(Fore.GREEN + Style.BRIGHT + message)

	time.sleep(2)
	DGText.printScan(Style.BRIGHT + Fore.CYAN + "Once the boss was destroyed,"
	" the rebellion was dismantled, letting the town recover!\n" + Style.RESET_ALL)
	time.sleep(2)

	defprntspd = 0.008
	creditScreen()
	time.sleep(2)
	DGExit()



def options():
	global playMusic
	questions = [
		{
			'type': 'list',
			'name': 'selection',
					'choices': ['Toggle Music',
								'Exit',],
			'message': 'What options would you like to toggle?',
		}
	]

	askLoop = 1
	while askLoop == 1:
		print(Style.RESET_ALL)
		answers = prompt(questions)
		# DGText.printScan_json(answers)
		userInput = answers['selection']
		# DGText.printScan(action + "You selected:" + userInput)
		if userInput == "Exit":
			askLoop = 0
			DGText.printScan(action + "You exited the options menu\n")

		elif userInput == "Toggle Music":
			playMusic = not playMusic
			if playMusic is False:
				endThreads()
			else:
				if Scene.current > 2:
					playSound("Music/quest.ogg", True)
				else:
					playSound("Music/intro.ogg", True)

			DGText.printScan("You toggled music to {value}\n".format(value=playMusic))




def save_game():
	# NOTE: If you want to add your own variable, transferred
	# across saves, please add it in the saveFile place.

	DGText.printScan(Style.BRIGHT + Fore.WHITE + "NOTE: This save function is a work in progress!"
	" It might not work as attended.\n")
	DGText.printScan(hint + "For example, '/home/user/save.json')")
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
			"absorbtion": Inventory.absorbtion,
			"events": events,
			"Scene.current": Scene.current,
			"Scene.description": Scene.description,
			"surroundingsLit": surroundingsLit,
			"Scene.hasCoins": Scene.hasCoins,
		}
	}

	with open(directory, 'w', encoding='utf-8') as f:
		json.dump(saveFile, f, ensure_ascii=False, indent=4)

	DGText.printScan(success + "Successfully saved to {dir}!\n".format(dir=directory))


def load_game():
	# NOTE: If you want to add your own variable, transferred
	# across saves, please add it to the global and then...

	global coins
	global Sword
	global armour
	global Inventory
	global events
	global Scene
	global surroundingsLit

	DGText.printScan(Style.BRIGHT + Fore.WHITE + "NOTE: This save function is a work in progress!"
	" It might not work as attended.\n")

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
	Inventory.absorbtion = saveFile['other']['absorbtion']
	events = saveFile['other']['events']
	Scene.current = saveFile['other']['Scene.current']
	Scene.description = saveFile['other']['Scene.description']
	surroundingsLit = saveFile['other']['surroundingsLit']
	Scene.hasCoins = saveFile['other']['Scene.hasCoins']

	DGText.printScan(DGText.success + "Successfully loaded save file!\n")


def checkCoins():
	global coins
	DGText.printScan(DGText.success + "You have $" + str(coins) + "!\n")
	if coins == 0:
		time.sleep(0.7)
		DGText.printScan(Style.BRIGHT + Fore.WHITE + "You have 0 coins? I feel bad, here"
			  " take 10 coins!")
		time.sleep(0.7)
		addCoins(10)
		time.sleep(0.7)


def openInventory():
	DGText.printScan(DGText.success + "Inventory:")

	DGText.printScan(DGText.success + "Your damage inflicted multipler is {m}x".format(m=Inventory.damage))
	DGText.printScan(DGText.success + "Your damage taken multiplyer is {p}x\n".format(p=Inventory.absorbtion))

	count = 0
	if Inventory.matches != 0:
		DGText.printScan(str(Inventory.matches) + " x Matches")

	if Inventory.sticks != 0:
		DGText.printScan(str(Inventory.sticks) + " x Sticks")

	if Inventory.basicHealingPotion != 0:
		DGText.printScan(str(Inventory.basicHealingPotion) + " x Basic Healing Potion")

	if Inventory.advancedHealingPotion !=0:
		DGText.printScan(str(Inventory.advancedHealingPotion) + " x Advanced Healing Potion")

	if Inventory.poisonPotion !=0:
		DGText.printScan(str(Inventory.poisonPotion) + " x Poison Healing Potion")

	if Inventory.sword == 1:
		DGText.printScan("Wooden Sword")

	if Inventory.sword == 2:
		DGText.printScan("Stone Sword")

	if Inventory.sword == 3:
		DGText.printScan("Iron Sword")

	elif Inventory.armour == 1:
		DGText.printScan("Copper Armour")

	elif Inventory.armour == 2:
		DGText.printScan("Iron Armour")


	# This DGText.printScan just adds some white space
	DGText.printScan(" ")


def purchase(storeSelected, id):
	global coins
	global absorbtion
	global damageMultiplyer

	item = storeSelected[id][0]
	price = storeSelected[id][1]
	if coins >= price:
		if item == "Matches":
			Inventory.matches = Inventory.matches + 1
		elif item == "Basic Healing Potion":
			Inventory.basicHealingPotion = Inventory.basicHealingPotion + 1

		elif item == "Advanced Healing Potion":
			Inventory.advancedHealingPotion = Inventory.advancedHealingPotion + 1

		elif item == "Poison Potion":
			Inventory.poisonPotion = Inventory.poisonPotion + 1

		elif item == "Copper Armour":
			if Inventory.armour == 1:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				Inventory.armour = 1
				Inventory.absorbtion = 0.8

		elif item == "Iron Armour":
			if Inventory.armour == 2:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				Inventory.armour = 2
				Inventory.absorbtion = 0.6

		elif item == "Stone Sword":
			if Inventory.sword == 2:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				Inventory.sword = 2
				Inventory.damage = 1.4

		elif item == "Iron Sword":
			if Inventory.sword == 3:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				Inventory.sword = 3
				Inventory.damage = 1.7


		DGText.printScan(action + "You purchased {item} for {price} coins!\n"
			  .format(item=item, price=price))
		coins = coins - price
	else:
		DGText.printScan(error + "You do not have enough coins to purchase this item!\n")


def openStore():
	initStore()
	DGText.printScan("You entered the store!")
	global CSSOptions
	global Inventory
	global coins
	global Scene
	DGText.printScan("------------------")
	DGText.printScan("	  STORE	   ")
	DGText.printScan("------------------")
	DGText.printScan(DGText.success + "You have $" + str(coins))
	for i in Scene.storeSelected:
		DGText.printScan(Fore.WHITE + "{name} -- {price}".format(name=i[0], price=i[1]))
	DGText.printScan("")

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
		print(Style.RESET_ALL)
		answers = prompt(questions)
		# DGText.printScan_json(answers)
		userInput = answers['itemChoice']
		# DGText.printScan(action + "You selected:" + userInput)
		if userInput == "Exit":
			askLoop = 0
			DGText.printScan(action + "You left the store.\n")
			Scene.storeSelected = []

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
		DGText.printScan(error + "You don't have any matches!\n")
	elif Scene.surroundingsLit == True:
		Inventory.matches = Inventory.matches - 1
		playSound("Sounds/matchUse.ogg", False)
		time.sleep(0.3)
		DGText.printScan("You light a match. it begins to burn away.")
		DGText.printScan(rip + "You used up one match. \n")

	elif Scene.surroundingsLit == False:
		Scene.description = "This place is in ruins, and it's possibly been like that for decades."
		Inventory.matches = Inventory.matches - 1
		Scene.surroundingsLit = True
		playSound("Sounds/matchUse.ogg", False)
		time.sleep(0.3)
		DGText.printScan("You Light a match, your surroundings fill up with light. "
			  "you can now see!")
		DGText.printScan(rip + "You used up one match. \n")
		if Scene.current == 1:
			print("")
			time.sleep(1)
			start()


def start():
	global Scene
	global Inventory

	Scene.storeSelected = []

	if Scene.surroundingsLit == False:
		DGText.printScan("You find yourself in an odd and dark place... \nWhat could this"
			  " possibly be?\n")
		Scene.description = "This place is extremely dark, you can't see anything..."
		time.sleep(1)

		DGText.printScan(
			"Check your Inventory, you might have something to \nimprove your vision...\n")
		time.sleep(1)
		if Inventory.matches < 1:
			DGText.printScan(rip + "You don't have any matches left!")
			time.sleep(1)
			DGText.printScan(rip + "There's no way to light this room.")
			time.sleep(1)
			DGText.printScan(action + "The only thing you can do is proceed to the next room...\n")
			time.sleep(1)
			questions = [
				{
					'type': 'confirm',
					'name': 'promptChoice',
					'message': 'Will you continue to the next room?',
				}
			]
			print(Style.RESET_ALL)
			theNewAnswer = prompt(questions)
			theNewResult = theNewAnswer['promptChoice']
			if theNewResult is True:
				DGText.printScan(action + "You proceed to the next room...\n")
				Scene.surroundingsLit = True

				Scene.current = Scene.current + 1

			else:
				DGText.printScan(action + "You do nothing...\n")

		# combat("Bob", 69)
		# DGText.printScan("Maybe I should use a match to light this place up...") # too straight forward.

		# DGText.printScan(hint + "type 'm' to use a match)\n" + Style.RESET_ALL) # too straight forward.
	else:
		if Scene.current == 1:
			# NOTE: describe this 'place'!
			DGText.printScan(Style.RESET_ALL + "This place looks like it's been abandoned decades ago...")
			# NOTE: describe this 'creature'! e.g. this oddly hunched over creature
			DGText.printScan(action + "An odd creature begins to walk up to you... \n")
			answer = ask("Should you hide or confront them?", "h", "c")
			if answer == "c":
				# User selected confront
				# Nothing special happens, it is passed on to the next part
				pass

			elif answer == "h":
				# User selected hide
				DGText.printScan(action + "You tried to hide, but there was nowhere to go, "
					  "the figure began to confront you.")
				time.sleep(1.5)

			DGText.printScan(action + "The odd figure got close enough until you "
				  "could see it.")  # NOTE: so is this a creature or figure
			time.sleep(1)

			DGText.printScan(action + "The figure looked like an ancient wizard. \n")
			time.sleep(1)

			DGText.printScan(hint + "type an answer)")
			input(Style.RESET_ALL + quote + 'Greetings, it seems you are new here,'
				  ' is that true?"\n' + Style.RESET_ALL) # this is kinda fucking retarded... the user doesn't even know its an input.
				  										 # I gave a hint to the user
			# NOTE: maybe. give the user a choice to say something.
			DGText.printScan(action + "You said yes. \n")
			time.sleep(0.7)

			DGText.printScan(quote + "I see, this is a dangerous place, so tread"
				  ' carefully..."')  # ITS DANGEROUS TO GO ALONE.
			time.sleep(1)

			DGText.printScan(quote + 'Here, take this, it will help you defend yourself."')
			time.sleep(2)  # TAKE THIS.

			DGText.printScan(DGText.success + "You recieved a basic Sword.")
			DGText.printScan(DGText.success + "You recieved a basic Healing Potion.")
			addCoins(50)

			Inventory.basicHealingPotion = Inventory.basicHealingPotion + 1
			Inventory.damage = 1.2
			Inventory.sword = 1
			Scene.current = Scene.current + 1
			time.sleep(2)

			# Add a new line
			print("")
			start()

		elif Scene.current == 2:
			DGText.printScan(action + "You ask the ancient wizard:")
			time.sleep(1)

			DGText.printScan(Style.RESET_ALL + "Who are you?")
			time.sleep(1)
			DGText.printScan("What is this place? \n")
			time.sleep(1)

			DGText.printScan(action + "The wizard responds \n")
			time.sleep(1.5)

			DGText.printScan(quote + 'This place is an underground town, it used to be'
				  ' thriving, there were plenty of stores, lots of jobs, it was'
				  ' a great place to be...\n But then, the rebellion came in'
				  ' and wiped this place out, everybody either escaped or died.\n'
				  ' And me, my name is Gylore, I was the founder of this town." \n')
			time.sleep(4)
			Scene.description = "This place is in ruins, apparently it's supposed to be a town...\nThere is a door to the next room, something seems to be strung across it."

			DGText.printScan(hint + "type an answer)")
			input(Style.RESET_ALL + quote + 'Would you like to recieve a quest?" \n'
				  + Style.RESET_ALL)
			quest.add("Obtain the Great Stone of Knowledge.")
			DGText.printScan(action + "You said yes. \n")
			time.sleep(0.8)

			DGText.printScan(quote + 'Try and recover the Great Stone of Knowledge,'
				  ' it is located in the north-east room, however it is guarded'
				  ' by very powerful Almogates." \n')
			time.sleep(3)

			DGText.printScan(quote + 'Good luck." \n')
			endThreads()
			playSound("Music/quest.ogg", True)
			time.sleep(1)

			DGText.printScan(action + "He leaves the room and now, you're on your own. \n")
			Scene.current = Scene.current + 1

		elif Scene.current == 3:
			initRandomRoom()
			randomEvent()
			Scene.current = Scene.current + 1


		elif Scene.current == 4:
			initRandomRoom()
			bombTrapScene()
			Scene.current = Scene.current + 1

		elif Scene.current == 5:
			initRandomRoom()
			randomEvent()
			Scene.current = Scene.current + 1


		elif Scene.current == 6:
			DGText.printScan(
				action + "You proceed to the next room, being very careful where you step.")


			Scene.hasCoins = True
			time.sleep(1)

			DGText.printScan(action + "You quickly hear a movement and freeze...\n")
			time.sleep(1)

			DGText.printScan(quote + 'IT WAS YOU WHO DID IT! Y-YOU WERE THE ONE WHO KILLED ALL M'
				  '-MY F-F-FRIENDS!"\n')
			time.sleep(1.5)
			DGText.printScan(action + "You try to explain that they were mistaken but"
				  " it was too late. \n")
			time.sleep(1)

			theResult = combat("Unidentified", 25, 5, 10)
			if theResult == "killed":
				DGText.printScan(
					action + "You killed the unknown person however, you can't stop feeling bad. \n")

			elif theResult == "flee":
				DGText.printScan(action + "You quickly ran away, you're safe now. \n")

			Scene.current = Scene.current + 1

		elif Scene.current == 7:
			# randomEvent() # random event here made some things confusing to a tester.
			print("This room is rather large. you should take a look around it.\n")
			Scene.canProgress = False
			Scene.current = Scene.current + 1
			Scene.description = "This room large and bare, but an old and dried up fountain lays ahead.\nA few coins lay scattered across the bottom, maybe you can pick them up? But however a single loose red brick in the wall north to you catches your eye..."

		elif Scene.current == 8:
			DGText.printScan(action + "You walk towards the massive door, slightly nervous"
			" about what you'll find there.")
			time.sleep(1.5)
			DGText.printScan(action + "A giant spider appears!")
			time.sleep(0.7)
			DGText.printScan(rip + "The spider spit acid on you!")
			time.sleep(0.6)
			damage(15)
			time.sleep(0.5)
			DGText.printScan(action + "There's nothing you can do other than fight!")
			spiderLoop = True
			while spiderLoop == True:
				# Start battle with 'Giant Spider'
				theResult = combat("Giant Spider", 35, 8, 12)
				if theResult == "killed":
					DGText.printScan(action + "Phew! That was hard! You prepare to move on... \n")
					spiderLoop = False

				elif theResult == "flee":
					DGText.printScan(action + "You've escaped, but the spider is determined to catch you!")
					time.sleep(1)
					DGText.printScan(action + "You try to run away from the spider however, you reach a dead end.")
					time.sleep(1)
					DGText.printScan(action + "You're forced into another battle!")
					time.sleep(1)

			Scene.current = Scene.current + 1

		elif Scene.current == 9:
			DGText.printScan(action + "You meet the wizard once again.")
			time.sleep(1)
			DGText.printScan(quote + 'MERLIN! how did you survive that!?"')
			time.sleep(1)
			DGText.printScan(action + "The wizard cast a spell on you that restored all your health.")
			time.sleep(0.5)
			heal(100)
			time.sleep(0.5)

			DGText.printScan(quote + "Anyways, I'm going to need someone to help me"
			" reconstruct the town however, \nthere's all of these dark wizards"
			" preventing me from doing so, \nthe only way I can defeat them"
			" is by obtaining the Great Stone of Knowledge.\"\n")
			time.sleep(2)
			DGText.printScan(quote + "I'm depending on you for this, I'm too weak"
			" to do it myself\"")
			time.sleep(1.5)
			DGText.printScan(Style.BRIGHT + "Gylore stated\n") # Gylore? you don't find his name anywhere though...
			DGText.printScan(quote + "Here, take this, it should help you buy the"
			" resources you need.")
			time.sleep(1)
			addCoins(50)

			Scene.current = Scene.current + 1

		elif Scene.current == 10:
			Scene.description = "This room is cold and empty. There isn't much but a door ahead."
			randomEvent()
			Scene.current = Scene.current + 1

		elif Scene.current == 11:
			Scene.description = "It looks to be brighter in here than the other rooms."
			randomEvent()
			Scene.current = Scene.current + 1

		elif Scene.current == 12:
			initRandomRoom()
			randomEvent()
			Scene.current = Scene.current + 1

		elif Scene.current == 13:
			randomEvent()
			Scene.current = Scene.current + 1

		elif Scene.current == 14:
			DGText.printScan(action + "You reach a room with a heavily guarded door.")
			time.sleep(1)
			DGText.printScan(action + "There is a guard protecting the door.")
			time.sleep(1)
			DGText.printScan(action + "You can either comfront the guard or wait"
			" and see if the guard will leave.\n")
			time.sleep(1)

			questions = [
				{
					'type': 'list',
					'name': 'userChoice',
							'choices': ["Comfront the guard",
										"Wait it out",],
					'message': 'What will you do?',
				}
			]

			print(Style.RESET_ALL)
			theAnswer = prompt(questions)
			userInput = theAnswer['userChoice']
			print(" ")

			if userInput == "Comfront the guard":
				DGText.printScan(action + "You comfront the guard and tell him about"
				" the quest you were given by Gylore.")
				time.sleep(0.7)
				DGText.printScan(action + "The guard called Gylore and has a conversation with him.")
				time.sleep(0.7)
				DGText.printScan(quote + "I see, I will let you through. Good luck"
				" with your journey.\"\n")
				Scene.current = Scene.current + 1
				time.sleep(0.7)

				DGText.printScan(action + "The door opened, revealing a thriving town.\n")
				Scene.description = "There is a marvolous, thriving town. It has beautiful lakes, lots of stores and a great community."

			else:
				DGText.printScan(action + "You wait several hours, hiding so the"
				" guard can't see you...")
				time.sleep(3)
				theLuck = random.randint(1, 3)
				if theLuck == 1:
					DGText.printScan(rip + "The guard spotted you!"
					" You have no time to explain yourself, you have to fight!\n")
					time.sleep(1)
					theResult = combat("Guard", 60, 3, 4)

					if theResult == "killed":
						DGText.printScan(action + "Now that there is no guard protecting"
						" the door, you can enter the next room.\n")
						time.sleep(1)
						Scene.current = Scene.current + 1
						Scene.description = "There is a marvolous, thriving town. It has beautiful lakes, lots of stores and a great community."

					elif theResult == "flee":
						DGText.printScan(action + "You ran away to the previous room.\n"
						"The only way you can proceed is by trying again.\n")

				else:
					DGText.printScan(action + "The guard doesn't leave. You have no"
					" other option but trying again.\n")

		elif Scene.current == 15:
			DGText.printScan(action + "You enter the town, birds are chirping,"
			" flowers are blooming, the rivers are flowing...")
			time.sleep(0.7)
			DGText.printScan(action + "It truly is a sight to behold!\n")
			time.sleep(0.7)

			DGText.printScan(action + "You look for the town hall, and begin to walk to it...")
			time.sleep(0.7)
			DGText.printScan(action + "Once you enter the town hall, a person asks you,")
			time.sleep(0.7)
			DGText.printScan(quote + "Welcome new visitor! How did you get here?\"")
			time.sleep(0.7)
			DGText.printScan(action + "You told them everything you saw.\n")
			time.sleep(0.7)

			DGText.printScan(action + "You ask them how this part of the town is"
			" thriving whereas the rest of the town was crippled.")
			time.sleep(0.7)
			DGText.printScan(quote + "Ah, you see, we've found the Rebellion's"
			" weakness, thorium!\nThorium is a highly radioactive material"
			" that the rebellion cannot withstand however, thorium is very"
			" difficult to obtain.\"\n")
			time.sleep(3)

			DGText.printScan(quote + "Good luck with your journey!\"\n")
			Scene.current = Scene.current + 1

		elif Scene.current == 16:
			DGText.printScan(action + "You quickly realise that this town"
			" is very small. There is not mcuh space to expand.\n")
			time.sleep(1)
			DGText.printScan(action + "You ask them why it is so small, they"
			" explain to you that they have ran out of thorium and at"
			" any moment, the rebellion can tear us to pieces.")
			time.sleep(1)
			DGText.printScan(quote + "There is a small deposit of Thorium nearby"
			" however, it is heavily guarded.\"\n")
			DGText.printScan(DGText.success + "You recieved a new quest!\n")
			quest.add("Delivier thorium to the town.")

			Scene.current = Scene.current + 1

		elif Scene.current == 17:
			DGText.printScan(action + "You leave this small town and further explore the dungeon.")
			DGText.printScan(action + "You feel a sense of danger, something is coming for you.\n")

			# aaaa idk what to put here

			Scene.current = Scene.current + 1

		else:
			DGText.printScan(DGText.success + "Thanks for testing DungeonCli!" + Fore.WHITE)
			DGText.printScan("We haven't finished this scene.")
			DGText.printScan("If you want to help us improve, feel free to send a screenshot or video of you")
			DGText.printScan("playing the game, at the discord server:")
			DGText.printScan(Style.BRIGHT + Fore.BLUE + "https://discord.gg/eAUqKKe\n")


def hpCheck():
	# Displays different colour depending on hp
	global hp
	if hp > 100:
		hp = 100

	hp = round(hp)

	if hp > 70:
		DGText.printScan(
			DGText.success + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))

	elif hp > 35:
		DGText.printScan(
			action + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))

	else:
		DGText.printScan(rip + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))


def randomEvent():
	global events
	global hasSeenAStore
	global Scene
	global storeSelected
	randomLoop = True

	DGText.printScan(action + "You proceed into the next room...\n")

	if len(events) > 0:
		selection = random.choice(events)
		if selection == "store":
			DGText.printScan(action + "You find a small store setup here")
			DGText.printScan(action + "Maybe they'll have something useful here..\n")
			Scene.description = Scene.description + " " + randomDialog.store(randomDialog)
			questions = [
				{
					'type': 'confirm',
					'name': 'promptChoice',
					'message': 'Will you enter the store?',
				}
			]

			print(Style.RESET_ALL)
			theAnswer = prompt(questions)
			theSelection = theAnswer['promptChoice']
			if theSelection is True:
				theLuck = random.randint(1, 5)
				if theLuck == 1:
					DGText.printScan(action + 'You knock on the door and ask to enter...')
					time.sleep(2)

					DGText.printScan(action + "Nobody responds...")
					time.sleep(0.8)
					DGText.printScan(action + "As you begin to walk away, you hear a slight hissing sound")
					time.sleep(0.8)
					DGText.printScan(rip + "A snake is trying to bite you!\n")
					time.sleep(0.8)
					combat("Snake", 20, 5, 15)

				else:
					DGText.printScan(action + 'You knock on the door and ask to enter...')
					time.sleep(2)

					# DGText.printScan(randomDialog.store(randomDialog))
					DGText.printScan(quote + 'Greetings! This place is in ruins however,'
					' I was able to setup a small store from the remains!"')
					time.sleep(0.8)
					openStore()



			else:
				DGText.printScan(action + "This seems too risky... you prepare to leave...\n")

		elif selection == "randomFight":
			DGText.printScan(action + "You hear a movement -- you freeze")
			time.sleep(0.6)
			DGText.printScan(action + "Someone is trying to attack you,")
			time.sleep(0.6)
			DGText.printScan(action + "It's too late to avoid a fight now!\n")
			time.sleep(0.6)
			randomEnemy()

		elif selection == "none":
			DGText.printScan(action + "You find absolutely nothing in this room...\n")


		elif selection == "bombTrap":
			bombTrapScene()

		elif selection == "wizardThatWantsToKillYou":
			#TODO: Finish this!
			DGText.printScan(quote + 'You. You have the information you need.\n'
				  '')
			pass

		elif selection == "treasure":

			DGText.printScan(action + "A massive Vault stands in this room.")
			time.sleep(1)
			DGText.printScan(action + "Something useful might be in it...")
			time.sleep(1)
			DGText.printScan(action + "Perhaps you could try break into it...\n")
			time.sleep(1)
			questions = [
				{
					'type': 'confirm',
					'name': 'promptChoice',
					'message': 'Will you try break into the vault?',
				}
			]

			print(Style.RESET_ALL)
			theAnswer = prompt(questions)
			theDecision = theAnswer['promptChoice']

			if theDecision is False:
				print("")
				DGText.printScan(action + "You think this is too risky and proceed to move on.\n")
			else:
				Scene.hasVault = True
				openVault()
				Scene.hasVault = False



		events = removeFromList(events, selection)

	else:
		DGText.printScan("There are no more unvisited events left!")

def openVault():
	if Scene.hasVault == True:
		theLuck = random.randint(1, 3)
		if theLuck == 1:
			DGText.printScan(action + "You spent several minutes trying to unlock the vault...")
			time.sleep(2)
			DGText.printScan(DGText.success + "You somehow unlock it!\n")
			time.sleep(0.6)
			DGText.printScan(action + "You walk into the vault but you are"
			" disappointed as it looks like someone has cleared out"
			" all the gold.\n")
			time.sleep(1)

		elif theLuck == 2:
			DGText.printScan(action + "You spent several minutes trying to unlock the vault...")
			time.sleep(2)
			DGText.printScan(DGText.success + "You somehow unlock it!\n")
			time.sleep(0.6)
			DGText.printScan(DGText.success + "You walk into the vault and you find"
			" hundreds of coins! You pick up as much as you can...")
			addCoins(50)

		elif theLuck == 3:
			DGText.printScan(action + "You spent several minutes trying to unlock the vault...")
			time.sleep(2)
			DGText.printScan(action + "You seem to be out of luck, however"
			" you've been spotted!\n")
			time.sleep(0.6)
			DGText.printScan(quote + 'YOU! STOP RIGHT THERE! YOU THIEF!"')
			DGText.printScan(Style.BRIGHT + "The Money Grinch shouted.\n")
			time.sleep(0.6)

			combat("Money Grinch", 30, 1, 30)
	else:
		DGText.printScan("There is no vault in this room...")


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

	# NOTE: This code would run, even if you would've fleed or died.
	# NOTE: That's why I've commented this out.
	# def __del__(self):
	# 	DGText.printScan("%s has died" % (self.name))

	def takeDamage(self, damage):
		self.health -= damage
		if (self.health <= 0):
			self.die()

	def die(self):
		del self

	def startBattle(self):
		combat(self.name, self.health, self.minDamage, self.maxDamage)



def randomEnemy():
	# [Name, Health, Enemy Minimum Damage, Enemy Maximum Damage]
	# enemyName, enemyHealth, enemyMinDamage, enemyMaxDamage
	# names = [["Unidentified", 25, 5, 10], ["Wizard", 40, 10, 20],
	#		 ["Giant Spider", 25, 5, 15], ["Bob", 100, 1, 1]]

	enemies = [Enemy("Unidentified", 25, 5, 10), Enemy("Wizard", 40, 7, 15),
	Enemy("Dark Wizard", 5, 25, 40), Enemy("Small Spider", 10, 4, 7)]

	enemy = random.choice(enemies)
	enemy.startBattle()
	#combat(decision[0], decision[1], decision[2], decision[3])


def lookAround():
	DGText.printScan(Scene.description + "\n")


def pickCoins():
	global Scene

	if Scene.hasCoins == True:
		amount = random.randint(10, 12)
		DGText.printScan(action + randomDialog.collectCoins(randomDialog))
		time.sleep(0.8)

		addCoins(amount)
		Scene.hasCoins = False

	else:
		DGText.printScan(error + "There are no coins to pick up! \n")


def usePoisonPotion():
	global Inventory
	theResult = 0
	if Inventory.poisonPotion != 0:
		DGText.printScan(DGText.success + "You have {amount} poison potions."
		.format(amount=Inventory.poisonPotion))

	questions = [
		{
			'type': 'list',
			'name': 'itemChoice',
					'choices': ["Poison Potion",
								"Exit",],
			'message': 'What potion would you like to use?',
		}
	]

	askLoop = True
	while askLoop:
		print(Style.RESET_ALL)
		theAnswer = prompt(questions)
		userInput = theAnswer['itemChoice']

		if userInput == "Exit":
			DGText.printScan("")
			askLoop = False
			return theResult


		elif userInput == "Poison Potion":
			if Inventory.poisonPotion > 0:
				theResult = theResult + 1
				DGText.printScan(rip + "You used up 1 poison potion")
				Inventory.poisonPotion = Inventory.poisonPotion - 1
				time.sleep(0.4)

			else:
				DGText.printScan(error + "You don't have any poison potions!")


def healingPotion():
	global Inventory
	theResult = 0


	if Inventory.basicHealingPotion != 0:
		DGText.printScan(DGText.success + "You have {amount} basic healing potions."
		.format(amount=Inventory.basicHealingPotion))

	if Inventory.advancedHealingPotion != 0:
		DGText.printScan(DGText.success + "You have {amount} advanced healing potions."
		.format(amount=Inventory.advancedHealingPotion))

	if Inventory.basicHealingPotion == 0 and Inventory.advancedHealingPotion == 0:
		DGText.printScan(DGText.error + "You don't have any potions!")
		askLoop = False
		return "notUsed"


	# Adds a new line
	print("")


	questions = [
		{
			'type': 'list',
			'name': 'itemChoice',
					'choices': ["Basic Healing Potion",
								"Advanced Healing Potion",
								'Exit'],
			'message': 'What potion would you like to use?',
		}
	]

	askLoop = True
	while askLoop:
		print(Style.RESET_ALL)
		theAnswer = prompt(questions)
		userInput = theAnswer['itemChoice']


		if userInput == "Exit":
			DGText.printScan("")
			askLoop = False
			return theResult


		elif userInput == "Basic Healing Potion":
			if Inventory.basicHealingPotion > 0:
				theResult = theResult + 1
				DGText.printScan(rip + "You used up 1 basic healing potion")
				Inventory.basicHealingPotion = Inventory.basicHealingPotion - 1
				heal(20)
				time.sleep(0.4)

			else:
				DGText.printScan(error + "You don't have any basic healing potions!\n")


		elif userInput == "Advanced Healing Potion":
			if Inventory.advancedHealingPotion > 0:
				theResult = theResult + 1
				DGText.printScan(rip + "You used up 1 advanced healing potion")
				Inventory.advancedHealingPotion = Inventory.advancedHealingPotion - 1
				heal(50)
				time.sleep(0.4)

			else:
				DGText.printScan(error + "You don't have any advanced healing potions!\n")


def skipIntro():
	Scene.current = 3
	endThreads()

	playSound("Music/quest.ogg", True)
	addCoins(50)

	global Inventory
	Scene.surroundingsLit = True
	Inventory.basicHealingPotion = Inventory.basicHealingPotion + 1
	Inventory.damage = 1.2
	Inventory.sword = 1
	quest.add("Obtain the Great Stone of Knowledge.")

def useSticks():
	# i'm gonna make this interesting and do something at some point.
	DGText.printScan(info + "These don't seem to do anything right now...\n")

def search():
	# i'm gonna make this interesting and do something at some point.
	if Scene.hasStore:
		DGText.printScan("This room has a store.\n")
	if Scene.hasCoins:
		DGText.printScan("There are some coins nearby...\n")
	else:
		DGText.printScan("You find nothing that interests you,\nI'd be better to"
		" move on...\n")

def listen():
	# i'm gonna make this interesting and do something at some point.
	# room specific dialog here maybe...
	DGText.printScan("It's extremely quiet, small drops of water reverb around the room...\n")

def endScreen():
	# print("╔════════════════════════════════════════════╗")
	# print("║                 {nameeeee}                 ║".format(nameeeee=(Style.BRIGHT + Fore.BLUE + "DungeonCli" + Style.RESET_ALL)))
	# print("╠════════════════════════════════════════════╣")
	# print("║                                            ║")
	# print("║     The classic command line experience    ║")
	# print("║                                            ║")
	# print("║       Made by some awesome people at       ║")
	# print("║                 pavela.net                 ║")
	# print("║                                            ║")
	# print("╚════════════════════════════════════════════╝")

	try:
		width = int(os.get_terminal_size().columns)
	except:
		width = 54
	a = int((width - 10) / 2)
	b = int(width + 10)

	print("".center(a,'-') + Style.BRIGHT + Fore.BLUE + "DungeonCli" + Style.RESET_ALL + "".center(a,'-'))
	print(Style.DIM + Fore.WHITE + version.center(width,' ') + Style.RESET_ALL)
	print(" ")
	print("Simulating the classic command line experience.".center(width,' '))
	print(" ")
	print("Made by the awesome DungeonCli team!".center(width,' '))
	print(("Join the discord! " + Fore.CYAN + "https://discord.gg/eAUqKKe" + Style.RESET_ALL).center(b,' '))
	print(" ")
	print((Fore.CYAN + "http://pavela.net:3000/Daniel/DungeonCli" + Style.RESET_ALL).center(b - 1,' '))
	print(" ")
	print("-".center(width,'-'))
	print(" ")

DGMain.EndScreen = endScreen # overwrite end screen.

	# THIS IS AN EXAMPLE. FEEL FREE TO CHANGE IT!

def creditScreen():
	try:
		width = int(os.get_terminal_size().columns)
	except:
		width = 54
	a = int((width - 10) / 2)
	b = int(width + 10)

	print("".center(a,'-') + Style.BRIGHT + Fore.BLUE + "DungeonCli" + Style.RESET_ALL + "".center(a,'-'))
	print(Style.DIM + Fore.WHITE + version.center(width,' ') + Style.RESET_ALL)
	DGText.printScan(" ")
	DGText.printScan("Simulating the classic command line experience.".center(width,' '))
	DGText.printScan(" ")
	DGText.printScan("Made by the awesome DungeonCli team!".center(width,' '))
	time.sleep(1)

	print("----".center(width, ' '))
	DGText.printScan("Main Programming - Daniel Pavela (Daniel071)".center(width,' '))
	DGText.printScan("Main Programming - Ethan \"Xenthio\" Cardwell".center(width,' '))
	DGText.printScan("General Programming - Mega27 (MCT32)".center(width,' '))
	DGText.printScan("General Programming - Ezray ".center(width,' '))
	DGText.printScan("Story - Daniel Pavela (Daniel071)".center(width,' '))
	DGText.printScan("Story - Ethan \"Xenthio\" Cardwell".center(width,' '))
	DGText.printScan("Sound effects - Ethan \"Xenthio\" Cardwell".center(width,' '))
	DGText.printScan("Music - Sine".center(width,' '))
	DGText.printScan("Music - AsianPotato77".center(width,' '))
	print("----".center(width, ' '))
	DGText.printScan("Developers Note".center(width,' '))
	DGText.printScan("Thanks so much Daniel for letting me help on this project!".center(width,' '))
	DGText.printScan("it was a blast to make. a great way for me to get back into python".center(width,' '))
	DGText.printScan("(I still prefer swift hahaha)".center(width,' '))
	DGText.printScan("Thank you so much - Ethan".center(width,' '))


	time.sleep(1)
	print("----".center(width, ' '))
	DGText.printScan("Self Promotion from Sine.".center(width,' '))
	DGText.printScan(("Youtube: " + Fore.CYAN + "https://www.youtube.com/channel/UCAK1pG_qcgqJd9d7BnayRtg" +
	Style.RESET_ALL).center(b - 1,' ')) # SELF PROMO LOOLLL


	print("-".center(width,'-'))
	DGText.printScan(" ")
	time.sleep(1)




def nextScene():
	if Scene.canProgress == True:
		Scene.hasStore = False

		start()
	else:
		DGText.printScan("Progress through where? there are no visible exits!")
		DGText.printScan(hint + "maybe try 'look' and see what you find...)\n" + Style.RESET_ALL)

def main():
	global Inventory
	detect_system()
	#defKey.stop()
	command = input(DGText.askPrompt + "[Action] " + Style.RESET_ALL)
	#defKey.start()
	if command in ("check money", "check coins", "coins", "money", "c"):
		checkCoins()

	elif command in ("open inventory", "open inv", "inventory", "inv", "i", "check inventory", "check inv", "pockets", "check pocket", "check pockets", "search pockets", "search pocket", "open pockets", "open pocket", "look in pocket", "look in pockets"):
		openInventory()

	elif command in ("use match", "strike match", "match", "light match", "use matches", "matches", "m"):
		useMatch()

	elif command in ("h", "help", "umm", "asdfghjkl", "qwertyuiop"):
		DGText.printScan("Help menu \n")

	elif command in ("e", "exit", "close", "alt-f4"):
		DGExit()

	elif command in ("hp", "health", "health points"):
		hpCheck()

	elif command in ("goto shop", "goto store", "store", "shop"):
		openStore()

	elif command in ("s", "start", "next", "proceed", "next room", "forth", "enter door", "go through door", "n"):
		richPrecense.present(Scene.current)
		nextScene()

	elif command in ("listen", "listen for sounds"):
		listen()

	elif command in ("search around", "search", "look for items", "search for items"):
		search()

	elif command in ("l", "look around", "look", "observe", "observe surroundings", "look at surroundings"):
		lookAround()

	elif command in ("pickup loose brick", "use loose brick", "use brick", "pickup brick", "brick"):
		useBrick()

	elif command in ("use sticks to light fire", "light fire with sticks"):
		DGText.printScan(error + "You cannot do that! The sticks are too wet...\n")

	elif command in ("use sticks", "sticks"):
		useSticks()

	elif command in ("cl_event", "plsevent"):
		# NOTE: This is for only debugging!
		if passwordPrompt() == "granted":
			randomEvent()

	elif command in ("cl_battle", "plsbattle"):
		# NOTE: This is for only debugging!
		if passwordPrompt() == "granted":
			randomEnemy()

	elif command in ("version", "ver"):
		DGText.printScan(version)

	elif command in ("pickup coins", "pick up coins", "pick coins"):
		pickCoins()

	elif command in ("heal", "potion"):
		healingPotion()

	elif command in ("cl_store", "plsstore"):
		# NOTE: This is for only debugging!
		if passwordPrompt() == "granted":
			openStore()

	elif command in ("cl_rich", "cl_addcoins", "plscoins"):
		DGText.printScan("The money grinch steps out of the shadows\n")
		time.sleep(1)
		DGText.printScan(quote + "In need of coins, eh? I mean i could let you have some of my precious coins, but ya gotta know the secret code.\"")
		DGText.printScan(" he said grouchingly\n")
		time.sleep(2)
		DGText.printScan(quote + "Go ahead. I'm waiting...\" \n")
		time.sleep(1)

		if passwordPrompt() == "granted":
			addCoins(200)
	elif command in ("cl_skipintro", "plsnointro"):
		if passwordPrompt() == "granted":
			skipIntro()

	elif command in ("save", "save game"):
		save_game()

	elif command in ("load", "load game"):
		load_game()
	elif command in ("plsdie", "plskill"):
		if passwordPrompt() == "granted":
			gameover()

	elif command in ("o", "options"):
		options()

	elif command in ("create torch", "make torch"):
		DGText.printScan(error + "You cannot do that! The sticks are too wet...\n")
	elif command in ("about", "us", "about us", "info"):
		endScreen()

	elif command in ("credits", "contributers", "people"):
		creditScreen()
	elif command in ("open the vault", "vault", "open vault", "use vault", "use the vault" "break in", "try to break in"):
		pass
		# openVault()

	elif command in ("plsop", "please make me OP"):
		if passwordPrompt() == "granted":
			addCoins(1000)
			Inventory.basicHealingPotion = 50
			Inventory.advancedHealingPotion = 50
			Inventory.poisonPotion = 50
			Inventory.sword = 2
			Inventory.damage = 1000.0
			Inventory.armour = 1
			Inventory.absorbtion = 0.01

	elif command in ("cls", "clear", "clear screen"):
		DGClear()

	elif command in ("quest", "check quests", "quests"):
		quest.list()

	elif command in ("boss battle", "plsboss"):
		if passwordPrompt() == "granted":
			bossBattle()

	elif command in ("success", "plswin"):
		if passwordPrompt() == "granted":
			bossSuccess()
	elif command in ("chat", "multiplayer"):
		multiplayer.runMe()

	else:
		invalidCommand()


detect_system()

if __name__ == '__main__':
	richPrecense.init()

	# Play moosic
	try:
		playSound("Music/intro.ogg", True)
	except:
		DGClear()
		DGText.printScan(error + "You need to have a ffmpeg installed for the music to work!")
		askLoop = True
		questions = [
			{
				'type': 'list',
				'name': 'userChoice',
						'choices': ['Install FFMPEG',
									'Disable Music',
									'Exit'],
				'message': 'What would you like to do?',
			}
		]

		while askLoop:
			print(Style.RESET_ALL)
			theAnswer = prompt(questions)
			theValue = theAnswer['userChoice']
			if theValue == "Install FFMPEG":
				if operatingsystem == 'windows':
					# TODO: Make an automated install script!
					DGText.printScan("NOTE: This installation requires Administrative priviledges"
					" because it needs to add ffmpeg to the path!\n")

					print(action + "Creating directories - 1/3..." + Style.RESET_ALL)
					os.system('md "%userprofile%\\ffmpeg')

					print(" ")
					print(action + "Downloading FFMPEG - 2/3..." + Style.RESET_ALL)
					print(action + "File 1 out of 3..." + Style.RESET_ALL)
					os.system('certutil.exe -urlcache -split -f "https://github.com/daniel071/ffmpeg-builds/releases/download/v1.0.0/ffmpeg.exe" "%userprofile%\\ffmpeg\\ffmpeg.exe"')

					print(" ")
					print(action + "File 2 out of 3..." + Style.RESET_ALL)
					os.system('certutil.exe -urlcache -split -f "https://github.com/daniel071/ffmpeg-builds/releases/download/v1.0.0/ffplay.exe" "%userprofile%\\ffmpeg\\ffplay.exe"')

					print(" ")
					print(action + "File 3 out of 3..." + Style.RESET_ALL)
					os.system('certutil.exe -urlcache -split -f "https://github.com/daniel071/ffmpeg-builds/releases/download/v1.0.0/ffprobe.exe" "%userprofile%\\ffmpeg\\ffprobe.exe"')

					print(" ")
					print(action + "Adding FFMPEG to Path - 3/3..." + Style.RESET_ALL)

					print(action + "Installing dependencies..." + Style.RESET_ALL)
					os.system('pip install pywin32')

					print(action + "Adding to path..." + Style.RESET_ALL)
					import win32com.shell.shell as shell
					commands = 'setx path "%path%;%userprofile%\\ffmpeg\\"'
					shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

					DGText.printScan(DGText.success + "Successfully installed FFMPEG!")
					DGText.printScan(Style.BRIGHT + Fore.BLUE + "NOTE: You must restart the command prompt"
					" so that the path would update!")
				else:
					DGText.printScan(error + "This script is not made for unix systems,"
					" if you have issues with music, please open an issue on github.")
					time.sleep(1)
					DGText.printScan(hint + "MacOS and most linux distros have FFMPEG pre-installed.\n")

			elif theValue == "Disable Music":
				playMusic = False
				askLoop = False
				DGText.printScan(DGText.success + "Successfully disabled music.")

			elif theValue == "Exit":
				askLoop = False
				DGExit()
				os._exit(1)



	#defKey.start()
	print("\r")
	DGClear()
	try:
		width = int(os.get_terminal_size().columns)
	except:
		width = 54
	a = int((width - 10) / 2)

	print("".center(a,'-') + Style.BRIGHT + Fore.BLUE + "DungeonCli" + Style.RESET_ALL + "".center(a,'-'))
	print("\r")

	# Introduce the user:
	DGText.printScan(Style.RESET_ALL + Style.BRIGHT + "Welcome to " + Fore.BLUE + "DungeonCli" + Style.RESET_ALL + " ")

	DGText.printScan(Style.DIM + Fore.WHITE + "==> " + version + "" + Style.RESET_ALL)
	print("")
	DGText.printScan("Type 'h' for help or 's' to start!")

	# Run those functions here:
	try:
		while mainLoop == 1:
			main()
	except:
		DGText.printScan(DGText.error + "An error has occured!")
		print(Fore.WHITE)
		time.sleep(0.3)
		DGText.printScan("Please copy this error and open up a new issue on Gitea!")
		time.sleep(0.3)
		DGText.printScan(Fore.BLUE + "Here: http://pavela.net:3000/Daniel/DungeonCli")
		time.sleep(1)
		print(Style.RESET_ALL + Fore.RED)
		raise


# This is the end of the code!
# Enjoy the meme corner below!

# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# FUCK YOU WHORE, WE LIKE FORTNITE, WE LIKE FORTNIE
# https://www.youtube.com/watch?v=GGmuA7PK-cc

# Our code is so THICC (:
# ░░░░░░░░░░▀▀▀██████▄▄▄░░░░░░░░░░
# ░░░░░░░░░░░░░░░░░▀▀▀████▄░░░░░░░
# ░░░░░░░░░░▄███████▀░░░▀███▄░░░░░
# ░░░░░░░░▄███████▀░░░░░░░▀███▄░░░
# ░░░░░░▄████████░░░░░░░░░░░███▄░░
# ░░░░░██████████▄░░░░░░░░░░░███▌░
# ░░░░░▀█████▀░▀███▄░░░░░░░░░▐███░
# ░░░░░░░▀█▀░░░░░▀███▄░░░░░░░▐███░
# ░░░░░░░░░░░░░░░░░▀███▄░░░░░███▌░
# ░░░░▄██▄░░░░░░░░░░░▀███▄░░▐███░░
# ░░▄██████▄░░░░░░░░░░░▀███▄███░░░
# ░█████▀▀████▄▄░░░░░░░░▄█████░░░░
# ░████▀░░░▀▀█████▄▄▄▄█████████▄░░
# ░░▀▀░░░░░░░░░▀▀██████▀▀░░░▀▀██░░

# what the fuck is the bottom of this document.
