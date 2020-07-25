# NOTE: JOIN THE DISCORD: https://discord.gg/eAUqKKe

# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!

# Import Libraries here:
#from __future__ import print_function, unicode_literals
#from __future__ import print_function
from colorama import Fore, Back, Style# type: ignore
from PyInquirer import prompt, print_json # type: ignore
import threading
import time
import random
import os
import sys
from src import richPrecense
from src import multiplayer
from Engine import *

# What??? this import fixed my error???
from Engine import DGSave
from Engine import DGUpdate

from sys import stdout
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
version = "Development Version 0.6.4"
# --------------------------

# Define variables here:

all_processes = []

# Used to prevent cheating:
devPassword = "hackerman"
developer = 0

invalidCommands = 0
mainLoop = 1
tempProgressCommand = ["nil"]

# TODO: when 'wizardThatWantsToKillYou' is done, add it here
events = ["store", "store", "store", "randomFight", "none", "none", "bombTrap",
"treasure", "treasure", "unknownCrate"]

CSSOptions = [["Matches", 5], ["Basic Healing Potion", 15],
			  ["Copper Armour", 75], ["Iron Armour", 125], ["Stone Sword", 60],
			  ["Iron Sword", 90],
			  ["Advanced Healing Potion", 60], ["Poison Potion", 20],
			  ["Lucky Coin", 550]]


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
		if len(quest.quests) < 1:
			printScan(DGText.error + "You don't have any quests so far")
		else:
			DGText.printScan(DGText.success + "Your current quests:")
			for theQuest in quest.quests:
				DGText.printScan(Style.BRIGHT + Fore.CYAN + theQuest)

		print(Style.RESET_ALL)


printspeed = 0.013
defprntspd = 0.013

def initRandomRoom():
	global DGDialog
	# Not my code but what I think it does is
	# has a 50% chance of placing coins in the room.
	# Also, there would be a 1 in 10 chance of the room not being lit
	global Scene
	a = random.randint(1,2)
	Scene.description = DGDialog.randomDialog.roomDescription()
	if a == 2:
		Scene.hasCoins == True
		Scene.description == Scene.description + " " + DGDialog.randomDialog.coinsOnFloor()
	b = random.randint(1,10)
	if b == 2:
		Scene.surroundingsLit == False


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


def bombTrapScene():
	global Scene
	global DGDialog

	Scene.description = "The room looked very charred after the explosion. you should probably proceed."

	DGMain.playSound("Sounds/explosion.ogg", False)
	DGText.printScan(rip + "BANG!")
	time.sleep(1)
	DGText.printScan(DGDialog.randomDialog.bombExplodes())
	damage(random.randint(5, 15) * DGPlayer.Inventory.absorbtion)
	time.sleep(1)


# Commands used
def bossBattle():
	global Scene
	global DGText
	endThreads()
	DGClear()

	DGText.printspeed = 0.05

	DGText.printScan(action + "The door behind you closes. There is no escape.")
	time.sleep(2)
	DGText.printScan(quote + "I've been expecting you. Any last words?\"\n")
	time.sleep(2)
	DGText.printScan(quote + "Nothing eh? You're too weak to defeat me,"
	" and there's nothing that can stop me.\"\n")

	DGMain.playSound("Music/bossBattle.ogg", True)

	DGText.printspeed = 0.7
	print(Style.BRIGHT + Fore.WHITE)
	DGText.printScan("\"goodbye.\"\n")
	DGText.printspeed = 0.013

	Scene.combatOverrideMusic = False
	bossLoop = True
	while bossLoop == True:
		theResult = DGCombat.combat("Boss", 25000, 1000, 1500)
		if theResult == "killed":
			bossSuccess()

		elif theResult == "flee":
			DGText.printScan(quote + "You think you can run away from me?\"")
			time.sleep(1)
			DGText.printScan(quote + "Think again.\"")
			time.sleep(1)

		endThreads()
		DGMain.playSound("Music/bossBattle.ogg", True)


def bossSuccess():
	global DGText

	endThreads()
	DGClear()
	DGMain.playSound("Music/endCredits.ogg", False)

	message = """
	__   __                     _       _
	\ \ / /__  _   _  __      _(_)_ __ | |
	 \ V / _ \| | | | \ \ /\ / / | '_ \| |
	  | | (_) | |_| |  \ V  V /| | | | |_|
	  |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)
	"""
	DGText.printScan(Fore.GREEN + Style.BRIGHT + message)

	DGText.printspeed = 0.020

	time.sleep(2.5)
	DGText.printScan(Style.BRIGHT + Fore.CYAN + "Once the boss was destroyed,"
	" the rebellion was dismantled, letting the town recover!\n" + Style.RESET_ALL)
	time.sleep(2.5)

	DGText.printspeed = 0.007
	creditScreen()
	time.sleep(2.5)
	DGExit()



def options():
	global DGMain
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
			DGMain.playMusic = not DGMain.playMusic
			if DGMain.playMusic is False:
				endThreads()
			else:
				if Scene.current > 2:
					DGMain.playSound("Music/quest.ogg", True)
				else:
					DGMain.playSound("Music/intro.ogg", True)

			DGText.printScan("You toggled music to {value}\n".format(value=DGMain.playMusic))


# TODO: Move these into DGPLayer as a player actions class.!

def checkCoins():
	global DGPlayer
	DGText.printScan(DGText.success + "You have $" + str(DGPlayer.coins) + "!\n")
	if DGPlayer.coins == 0:
		time.sleep(0.7)
		DGText.printScan(Style.BRIGHT + Fore.WHITE + "You have 0 coins? I feel bad, here"
			  " take 10 coins!")
		time.sleep(0.7)
		DGMain.addCoins(10)
		time.sleep(0.7)


def openInventory():
	DGText.printScan(DGText.success + "Inventory:")

	DGText.printScan(DGText.success + "Your damage inflicted multipler is {m}x".format(m=DGPlayer.Inventory.damage))
	DGText.printScan(DGText.success + "Your damage taken multiplyer is {p}x".format(p=DGPlayer.Inventory.absorbtion))
	DGText.printScan(DGText.success + "Your money multiplyer is {p}x\n".format(p=DGPlayer.Inventory.moneyMultiplyer))

	count = 0
	if DGPlayer.Inventory.matches != 0:
		DGText.printScan(str(DGPlayer.Inventory.matches) + " x Matches")

	if DGPlayer.Inventory.sticks != 0:
		DGText.printScan(str(DGPlayer.Inventory.sticks) + " x Sticks")

	if DGPlayer.Inventory.basicHealingPotion != 0:
		DGText.printScan(str(DGPlayer.Inventory.basicHealingPotion) + " x Basic Healing Potion")

	if DGPlayer.Inventory.advancedHealingPotion !=0:
		DGText.printScan(str(DGPlayer.Inventory.advancedHealingPotion) + " x Advanced Healing Potion")

	if DGPlayer.Inventory.poisonPotion !=0:
		DGText.printScan(str(DGPlayer.Inventory.poisonPotion) + " x Poison Healing Potion")

	if DGPlayer.Inventory.sword == 1:
		DGText.printScan("Wooden Sword")

	if DGPlayer.Inventory.sword == 2:
		DGText.printScan("Stone Sword")

	if DGPlayer.Inventory.sword == 3:
		DGText.printScan("Iron Sword")

	elif DGPlayer.Inventory.armour == 1:
		DGText.printScan("Copper Armour")

	elif DGPlayer.Inventory.armour == 2:
		DGText.printScan("Iron Armour")

	if DGPlayer.Inventory.secretKey == 1:
		DGText.printScan("Random Key?")


	# This DGText.printScan just adds some white space
	DGText.printScan(" ")

def purchase(storeSelected, id):
	global DGPlayer
	global absorbtion
	global damageMultiplyer

	item = storeSelected[id][0]
	price = storeSelected[id][1]
	if DGPlayer.coins >= price:
		if item == "Matches":
			DGPlayer.Inventory.matches = DGPlayer.Inventory.matches + 1
		elif item == "Basic Healing Potion":
			DGPlayer.Inventory.basicHealingPotion = DGPlayer.Inventory.basicHealingPotion + 1

		elif item == "Advanced Healing Potion":
			DGPlayer.Inventory.advancedHealingPotion = DGPlayer.Inventory.advancedHealingPotion + 1

		elif item == "Poison Potion":
			DGPlayer.Inventory.poisonPotion = DGPlayer.Inventory.poisonPotion + 1

		elif item == "Copper Armour":
			if DGPlayer.Inventory.armour == 1:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				DGPlayer.Inventory.armour = 1
				DGPlayer.Inventory.absorbtion = 0.8

		elif item == "Iron Armour":
			if DGPlayer.Inventory.armour == 2:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				DGPlayer.Inventory.armour = 2
				DGPlayer.Inventory.absorbtion = 0.6

		elif item == "Stone Sword":
			if DGPlayer.Inventory.sword == 2:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				DGPlayer.Inventory.sword = 2
				DGPlayer.Inventory.damage = 1.4

		elif item == "Iron Sword":
			if DGPlayer.Inventory.sword == 3:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				DGPlayer.Inventory.sword = 3
				DGPlayer.Inventory.damage = 1.7

		elif item == "Lucky Coin":
			if DGPlayer.Inventory.moneyMultiplyer == 2:
				DGText.printScan(error + "You already have this item!\n")
				return "bruh"
			else:
				DGPlayer.Inventory.moneyMultiplyer = 2



		DGText.printScan(action + "You purchased {item} for {price} coins!\n"
			  .format(item=item, price=price))
		DGPlayer.coins = DGPlayer.coins - price
	else:
		DGText.printScan(error + "You do not have enough coins to purchase this item!\n")


def openStore():
	initStore()
	DGText.printScan("You entered the store!")
	global CSSOptions
	global DGPlayer
	global Scene
	DGText.printScan("------------------")
	DGText.printScan("	  STORE	   ")
	DGText.printScan("------------------")
	DGText.printScan(DGText.success + "You have $" + str(DGPlayer.coins))
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
	global DGPlayer
	global surroundingsLit
	global Scene

	if DGPlayer.Inventory.matches == 0:
		DGText.printScan(error + "You don't have any matches!\n")
	elif Scene.surroundingsLit == True:
		DGPlayer.Inventory.matches = DGPlayer.Inventory.matches - 1
		DGMain.playSound("Sounds/matchUse.ogg", False)
		time.sleep(0.3)
		DGText.printScan("You light a match. it begins to burn away.")
		DGText.printScan(rip + "You used up one match. \n")

	elif Scene.surroundingsLit == False:
		Scene.description = "This place is in ruins, and it's possibly been like that for decades."
		DGPlayer.Inventory.matches = DGPlayer.Inventory.matches - 1
		Scene.surroundingsLit = True
		DGMain.playSound("Sounds/matchUse.ogg", False)
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
	global DGPlayer
	global DGText
	global tempProgressCommand

	Scene.storeSelected = []

	if Scene.surroundingsLit == False:
		DGText.printScan(DGText.action + "You are lying down, the cold, wet floor pressed"
		" against your face..." + Style.RESET_ALL + "\nWhere are you?\n")
		Scene.description = "It is extremely dark and cold \n(however that could be because of your wet clothes), but despite that you can't see a single thing..."
		time.sleep(1)

		DGText.printScan(DGText.action + "You get up, your footsteps echo through out the room. It's Extremely dark.")
		DGText.printScan(Style.RESET_ALL + "Check your Inventory, you might have something to improve your vision...\n")
		time.sleep(1)
		if DGPlayer.Inventory.matches < 1:
			DGText.printScan(rip + "You don't have any matches left!")
			time.sleep(1)
			DGText.printScan(rip + "There's no way to light this room.")
			time.sleep(1)
			DGText.printScan(action + "The only thing you can do is proceed to the next room...\n")
			Scene.canProgress == True

	else:
		if Scene.current == 1:
			DGText.printScan(Style.RESET_ALL + "The Light is bright enough to "
			"see where you are walking, no walls are nearby.")
			DGText.printScan(action + "While being scared, you think it is "
			"probably safe enough to \nwander about your surroundings a bit... \n")
			tempProgressCommand = ["walk around", "wander", "walk", "wonder"]


		elif Scene.current == 2:
			DGText.printScan(DGText.action + "You start to take a small wander and look around.")
			time.sleep(0.75)
			DGText.printScan(DGText.action + "After wandering around for some time, something shiny catches your attention.\n")
			time.sleep(0.75)

			DGText.printScan(Style.RESET_ALL + "It's a lock, it hangs losely on a chest. It's extremely "
			"rusted to the point where the fact that\nit's shine caught your eye is astounding.\n")
			tempProgressCommand = ["break lock", "attempt to open", "open",
			"open chest", "unlock", "unlock chest", "pick", "pick lock"]
			time.sleep(1)

		elif Scene.current == 3:
			DGText.printScan(DGText.action + "The lock snaps off. you gently lift up the lid and take what is inside.")
			DGText.printScan(success + "You pickup a basic healing potion and"
			" a wooden sword.")
			DGPlayer.Inventory.basicHealingPotion = DGPlayer.Inventory.basicHealingPotion + 1
			DGPlayer.Inventory.damage = 1.2
			DGPlayer.Inventory.sword = 1
			time.sleep(2)

			# Add a new line
			print("")


		elif Scene.current == 4:
			DGText.printScan(DGText.action + "You carefully proceed into the next room...")
			time.sleep(1)
			DGText.printScan(Style.RESET_ALL + "It is completely empty. There is no sound except"
			" the water dripping...\n")
			time.sleep(1)
			DGText.printScan(DGText.rip + "Suddenly, a goblin bursts through"
			" the other door!")
			time.sleep(0.5)
			DGText.printScan(DGText.rip + "There's nothing you can do other than"
			" fight!\n")
			time.sleep(0.2)

			DGCombat.combat("Anomynous Goblin", 20, 3, 5)


		elif Scene.current == 5:
			DGText.printScan(DGText.action + "You find a small outpost here. There are unknown creatures"
			" scattered across the place")
			DGText.printScan(Style.RESET_ALL + "The outpost seems to be in ruins,"
			" blood scattered across the wall of burned down houses.\n")
			time.sleep(1)
			DGText.printScan(Style.BRIGHT + Fore.WHITE + "Theres a sign on a dusty wall, it reads,\n")

			DGText.printspeed = 0.05

			DGText.printScan(DGText.quote +
			"It used to be great here,\n"
			"But then, the rebellion wiped us clear,\n"
			"There's only one way back,\n"
			"It's simple yet hard,\n"
			"Defeat the guard.\"\n")

			DGText.printspeed = 0.013

			time.sleep(1)
			DGText.printScan(DGText.action + "Suddenly, some sort of 'creature'"
			" comes up to you. It can't speak English, but it's pointing towards"
			" a trapdoor.")

			questions = [
				{
					'type': 'confirm',
					'name': 'promptChoice',
					'message': 'Will you climb down onto the trapdoor?',
				}
			]

			print(Style.RESET_ALL)
			theAnswer = prompt(questions)
			theSelection = theAnswer['promptChoice']
			if theSelection is True:
				DGText.printScan(DGText.success + "You climb down onto the trapdoor."
				" Once you reach the bottom, you found a key!")
				DGText.printScan(DGText.action + "You don't know what this key is for,"
				" but you take it anyway.\n")
				DGPlayer.Inventory.secretKey = 1

				time.sleep(2)

				DGText.printScan(Style.RESET_ALL + "As you begin to exit the trapdoor...\n")

				bombTrapScene()


			else:
				DGText.printScan(DGText.action + "You decide it is too risky and"
				" prepare to move on.\n")


		# elif Scene.current == 6:

		else:
			DGText.printScan(success + "Thanks for testing DungeonCli!" + Fore.WHITE)
			DGText.printScan("We haven't finished this scene.")
			DGText.printScan("If you want to help us improve, feel free to send a screenshot or video of you")
			DGText.printScan("playing the game, at the discord server:")
			DGText.printScan(Style.BRIGHT + Fore.BLUE + "https://discord.gg/eAUqKKe\n")


def randomEvent():
	global events
	global hasSeenAStore
	global Scene
	global storeSelected
	global DGDialog
	randomLoop = True

	DGText.printScan(action + "You proceed into the next room...\n")

	if len(events) > 0:
		selection = random.choice(events)
		if selection == "store":
			DGText.printScan(DGText.action + "You find a small store setup here")
			DGText.printScan(DGText.action + "Maybe they'll have something useful here..\n")
			Scene.description = Scene.description + " " + DGDialog.randomDialog.store()
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
					DGText.printScan(DGText.action + 'You knock on the door and ask to enter...')
					time.sleep(2)

					DGText.printScan(DGText.action + "Nobody responds...")
					time.sleep(0.8)
					DGText.printScan(DGText.action + "As you begin to walk away, you hear a slight hissing sound")
					time.sleep(0.8)
					DGText.printScan(DGText.rip + "A snake is trying to bite you!\n")
					time.sleep(0.8)
					DGCombat.combat("Snake", 20, 5, 15)

				else:
					DGText.printScan(DGText.action + 'You knock on the door and ask to enter...')
					time.sleep(2)

					# DGText.printScan(randomDialog.store(randomDialog))
					DGText.printScan(DGText.quote + 'Greetings! This place is in ruins however,'
					' I was able to setup a small store from the remains!"')
					time.sleep(0.8)
					openStore()



			else:
				DGText.printScan(DGText.action + "This seems too risky... you prepare to leave...\n")

		elif selection == "randomFight":
			DGText.printScan(DGText.action + "You hear a movement -- you freeze")
			time.sleep(0.6)
			DGText.printScan(DGText.action + "Someone is trying to attack you,")
			time.sleep(0.6)
			DGText.printScan(DGText.action + "It's too late to avoid a fight now!\n")
			time.sleep(0.6)
			randomEnemy()

		elif selection == "none":
			DGText.printScan(action + "You find absolutely nothing in this room...\n")


		elif selection == "bombTrap":
			DGText.printScan(action + "It is odly quiet here... you begin to look around... \n")
			time.sleep(2)
			bombTrapScene()

		elif selection == "wizardThatWantsToKillYou":
			#TODO: Finish this!
			DGText.printScan(DGText.quote + 'You. You have the information you need.\n'
				  '')
			pass

		elif selection == "treasure":

			DGText.printScan(DGText.action + "A massive Vault stands in this room.")
			time.sleep(1)
			DGText.printScan(DGText.action + "Something useful might be in it...")
			time.sleep(1)
			DGText.printScan(DGText.action + "Perhaps you could try break into it...\n")
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
				DGText.printScan(DGText.action + "You think this is too risky and proceed to move on.\n")
			else:
				Scene.hasVault = True
				openVault()
				Scene.hasVault = False


		elif selection == "unknownCrate":
			global DGPlayer

			DGText.printScan(DGText.action + "You find a mysterious crate...")

			questions = [
				{
					'type': 'confirm',
					'name': 'promptChoice',
					'message': 'Will you open it?',
				}
			]

			print(Style.RESET_ALL)
			theAnswer = prompt(questions)
			theDecision = theAnswer['promptChoice']

			if theDecision is False:
				print("")
				DGText.printScan(DGText.action + "You think this is too risky and proceed to move on.\n")

			else:
				areYaLucky = random.randint(1, 5)
				if areYaLucky == 1:
					# You get free loot
					lootGoodies = ["Stone sword", "Iron armour"]
					chosenGoodies = random.choice(lootGoodies)

					DGText.printScan(DGText.success + "You open the chest and find {item}!"
					.format(item=chosenGoodies))

					if chosenGoodies == "Stone sword":
						if DGPlayer.Inventory.sword >= 3:
							DGText.printScan(error + "You already have this item!\n")
						else:
							DGPlayer.Inventory.sword = 3
							DGPlayer.Inventory.damage = 1.7

					elif chosenGoodies == "Iron armour":
						if DGPlayer.Inventory.armour >= 2:
							DGText.printScan(error + "You already have this item!\n")
						else:
							DGPlayer.Inventory.armour = 2
							DGPlayer.Inventory.absorbtion = 0.6

				elif areYaLucky == 2:
					# You get free gold
					DGText.printScan(DGText.success + "You open the chest and you find free gold!")
					DGMain.addCoins(random.randint(100, 120))

				elif areYaLucky == 3:
					# You get nothing
					DGText.printScan(DGText.rip + "You open the chest and find nothing.")
					DGText.printScan(DGText.action + "You move on...\n")

				else:
					# It's a bomb!
					DGText.printScan(DGText.action + "You open the chest and find nothing.")
					DGText.printScan(DGText.action + "You hear a sound...")
					bombTrapScene()


		events = removeFromList(events, selection)

	else:
		DGText.printScan("There are no more unvisited events left!")

def openVault():
	if Scene.hasVault == True:
		theLuck = random.randint(1, 3)
		if theLuck == 1:
			DGText.printScan(DGText.action + "You spent several minutes trying to unlock the vault...")
			time.sleep(2)
			DGText.printScan(DGText.success + "You somehow unlock it!\n")
			time.sleep(0.6)
			DGText.printScan(DGText.action + "You walk into the vault but you are"
			" disappointed as it looks like someone has cleared out"
			" all the gold.\n")
			time.sleep(1)

		elif theLuck == 2:
			DGText.printScan(DGText.action + "You spent several minutes trying to unlock the vault...")
			time.sleep(2)
			DGText.printScan(DGText.success + "You somehow unlock it!\n")
			time.sleep(0.6)
			DGText.printScan(DGText.success + "You walk into the vault and you find"
			" hundreds of coins! You pick up as much as you can...")
			DGMain.addCoins(50)

		elif theLuck == 3:
			DGText.printScan(DGText.action + "You spent several minutes trying to unlock the vault...")
			time.sleep(2)
			DGText.printScan(DGText.action + "You seem to be out of luck, however"
			" you've been spotted!\n")
			time.sleep(0.6)
			DGText.printScan(DGText.quote + 'YOU! STOP RIGHT THERE! YOU THIEF!"')
			DGText.printScan(Style.BRIGHT + "The Money Grinch shouted.\n")
			time.sleep(0.6)

			DGCombat.combat("Money Grinch", 30, 1, 30)
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

	def takeDamage(self, damage):
		self.health -= damage
		if (self.health <= 0):
			self.die()

	def die(self):
		del self

	def startBattle(self):
		DGCombat.combat(self.name, self.health, self.minDamage, self.maxDamage)



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
		DGText.printScan(action + DGDialog.randomDialog.collectCoins())
		time.sleep(0.8)

		DGMain.addCoins(amount)
		Scene.hasCoins = False

	else:
		DGText.printScan(error + "There are no coins to pick up! \n")



def skipIntro():
	Scene.current = 3
	endThreads()

	DGMain.playSound("Music/quest.ogg", True)
	DGMain.addCoins(50)

	global DGPlayer
	Scene.surroundingsLit = True
	DGPlayer.Inventory.basicHealingPotion = DGPlayer.Inventory.basicHealingPotion + 1
	DGPlayer.Inventory.damage = 1.2
	DGPlayer.Inventory.sword = 1
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
	#DGText.printScan("Self Promotion from Sine:".center(width,' '))
	#DGText.printScan(("Youtube: " + Fore.CYAN + "https://www.youtube.com/channel/UCAK1pG_qcgqJd9d7BnayRtg" +
	#Style.RESET_ALL).center(b - 1,' ')) # SELF PROMO LOOLLL
	#DGText.printScan("Self Promotion from AsianPotato77:".center(b - 1,' '))
	#DGText.printScan(("SoundCloud:" + Fore.CYAN + "https://soundcloud.com/s-z-174676229").center(b - 1,' ') + Style.RESET_ALL)
	# STOP THE SELF PROMOTIONS! IT LOOKS DUMB! ALSO IM GONNA DO THE STORY CHANGE SOON I KEEP FORGETTING!!
	# Daniel - The artists made the song and I think if people are interested
	# Daniel - in listening to their music they can visit it,
	# Daniel - Also why are we talking in comments?

	print("-".center(width,'-'))
	DGText.printScan(" ")
	time.sleep(1)




def nextScene():
	global Scene

	if Scene.canProgress == True:
		Scene.hasStore = False
		Scene.current = Scene.current + 1
		start()
	else:
		DGText.printScan("Progress through where? there are no visible exits!")
		DGText.printScan(hint + "maybe try 'look' and see what you find...)\n" + Style.RESET_ALL)


def main():
	global DGPlayer
	global DGSave
	global tempProgressCommand

	command = input(DGText.askPrompt + "[Action] " + Style.RESET_ALL)

	if command in tempProgressCommand and command != "nil":
		richPrecense.present(Scene.current)
		tempProgressCommand = ["nil"]
		nextScene()

	elif command in ("check money", "check coins", "coins", "money", "c"):
		checkCoins()

	elif command in ("open inventory", "open inv", "inventory", "inv", "i", "check inventory", "check inv", "pockets", "check pocket", "check pockets", "search pockets", "search pocket", "open pockets", "open pocket", "look in pocket", "look in pockets"):
		openInventory()

	elif command in ("use match", "strike match", "match", "light match", "use matches", "matches", "m"):
		useMatch()

	elif command in ("h", "help", "umm", "asdfghjkl", "qwertyuiop"):
		DGText.printScan(Fore.BLUE + Style.BRIGHT + "Thanks for testing DungeonCli!")
		DGText.printScan(Fore.GREEN + "Here are some common commands:")
		DGText.printScan(Style.RESET_ALL + "\n--------\n" + Style.BRIGHT)

		DGText.printScan(Fore.BLUE + "hp: " + Fore.WHITE + "Checks your current health")
		DGText.printScan(Fore.BLUE + "coins: " + Fore.WHITE + "Checks your current balance")
		DGText.printScan(Fore.BLUE + "start: " + Fore.WHITE + "Proceeds to next scene")
		DGText.printScan(Fore.BLUE + "inventory: " + Fore.WHITE + "Shows your stats in inventory")
		DGText.printScan(Fore.BLUE + "potion: " + Fore.WHITE + "Lets you use a healing potion")
		DGText.printScan(Fore.BLUE + "hp: " + Fore.WHITE + "Checks your current health")
		DGText.printScan(Fore.BLUE + "quests: " + Fore.WHITE + "Shows your current quests")
		DGText.printScan(Fore.BLUE + "credits: " + Fore.WHITE + "Info about the developers")
		DGText.printScan(Fore.BLUE + "about: " + Fore.WHITE + "About the game")

		DGText.printScan(Style.RESET_ALL + "\n--------\n" + Style.BRIGHT)

	elif command in ("e", "exit", "close", "alt-f4"):
		DGExit()

	elif command in ("hp", "health", "health points"):
		DGMain.hpCheck()

	elif command in ("goto shop", "goto store", "store", "shop"):
		openStore()

	elif command in ("s", "start", "next", "proceed", "next room", "forth", "enter door", "go through door", "n"):
		if tempProgressCommand[0] == "nil":
			richPrecense.present(Scene.current)
			nextScene()
		else:
			# FIXME: This may be confusing, but I cant come up with anything better
			DGText.printScan(DGText.error + "Try something else...\n")

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
		DGPotion.healingPotion()

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
			DGMain.addCoins(2000)

	elif command in ("cl_skipintro", "plsnointro"):
		if passwordPrompt() == "granted":
			skipIntro()

	elif command in ("save", "save game"):
		DGSave.save()

	elif command in ("load", "load game"):
		DGSave.load()

	elif command in ("plsdie", "plskill"):
		if passwordPrompt() == "granted":
			DGMain.gameover()

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
			DGMain.addCoins(1000)
			DGPlayer.Inventory.basicHealingPotion = 50
			DGPlayer.Inventory.advancedHealingPotion = 50
			DGPlayer.Inventory.poisonPotion = 50
			DGPlayer.Inventory.sword = 2
			DGPlayer.Inventory.damage = 1000.0
			DGPlayer.Inventory.armour = 1
			DGPlayer.Inventory.absorbtion = 0.01

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

	elif command in ("debug", "devDebug"):
		print("Current scene:", DGScene.current)
		print("Temp Progress Command:",  tempProgressCommand)
	elif command in ("update", "new"):
		DGUpdate.update()


	else:
		invalidCommand()


operatingsystem = detect_system()

if __name__ == '__main__':

	richPrecense.init()

	# Play moosic
	try:
		DGMain.playSound("Music/intro.ogg", True)
	except:
		DGClear()
		DGText.printScan(DGText.error + "You need to have a ffmpeg installed for the music to work!")
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
					DGText.printScan("NOTE: This installation requires Administrative priviledges"
					" because it needs to add ffmpeg to the path!\n")

					print(DGText.loading + "Creating directories - 1/3..." + Style.RESET_ALL)
					os.system('md "%userprofile%\\ffmpeg')

					print(" ")
					print(DGText.loading + "Downloading FFMPEG - 2/3..." + Style.RESET_ALL)
					print(DGText.action + "File 1 out of 3..." + Style.RESET_ALL)
					os.system('certutil.exe -urlcache -split -f "https://github.com/daniel071/ffmpeg-builds/releases/download/v1.0.0/ffmpeg.exe" "%userprofile%\\ffmpeg\\ffmpeg.exe"')

					print(" ")
					print(DGText.action + "File 2 out of 3..." + Style.RESET_ALL)
					os.system('certutil.exe -urlcache -split -f "https://github.com/daniel071/ffmpeg-builds/releases/download/v1.0.0/ffplay.exe" "%userprofile%\\ffmpeg\\ffplay.exe"')

					print(" ")
					print(DGText.action + "File 3 out of 3..." + Style.RESET_ALL)
					os.system('certutil.exe -urlcache -split -f "https://github.com/daniel071/ffmpeg-builds/releases/download/v1.0.0/ffprobe.exe" "%userprofile%\\ffmpeg\\ffprobe.exe"')

					print(" ")
					print(DGText.loading + "Adding FFMPEG to Path - 3/3..." + Style.RESET_ALL)

					print(DGText.loading + "Installing dependencies..." + Style.RESET_ALL)
					os.system('python -m pip install pywin32')

					print(DGText.loading + "Adding to path..." + Style.RESET_ALL)
					import win32com.shell.shell as shell
					commands = 'setx path "%path%;%userprofile%\\ffmpeg\\"'
					shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

					DGText.printScan(DGText.success + "Successfully installed FFMPEG!")
					DGText.printScan(Style.BRIGHT + Fore.BLUE + "NOTE: You must restart the command prompt"
					" so that the path would update!")
				else:
					DGText.printScan(DGText.error + "This script is not made for unix systems,"
					" if you have issues with music, please open an issue on gitea.")
					time.sleep(1)
					DGText.printScan(DGText.hint + "MacOS and most linux distros have FFMPEG pre-installed.\n")

			elif theValue == "Disable Music":
				DGMain.playMusic = False
				askLoop = False
				DGText.printScan(DGText.success + "Successfully disabled music.")

			elif theValue == "Exit":
				askLoop = False
				DGExit()
				os._exit(1)


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
		time.sleep(0.3)
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
