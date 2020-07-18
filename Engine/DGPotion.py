# Includes functions for all the potion stuff

from . import DGText
from . import DGMain
from . import DGPlayer
from colorama import Fore, Back, Style
from colorama import init
from PyInquirer import prompt, print_json
import time

def healingPotion():
	global DGPlayer
	theResult = 0


	if DGPlayer.Inventory.basicHealingPotion != 0:
		DGText.printScan(DGText.success + "You have {amount} basic healing potions."
		.format(amount=DGPlayer.Inventory.basicHealingPotion))

	if DGPlayer.Inventory.advancedHealingPotion != 0:
		DGText.printScan(DGText.success + "You have {amount} advanced healing potions."
		.format(amount=DGPlayer.Inventory.advancedHealingPotion))

	if DGPlayer.Inventory.basicHealingPotion == 0 and DGPlayer.Inventory.advancedHealingPotion == 0:
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
			if DGPlayer.Inventory.basicHealingPotion > 0:
				theResult = theResult + 1
				DGText.printScan(DGText.rip + "You used up 1 basic healing potion")
				DGPlayer.Inventory.basicHealingPotion = DGPlayer.Inventory.basicHealingPotion - 1
				DGPlayer.heal(20)
				time.sleep(0.4)

			else:
				DGText.printScan(DGText.error + "You don't have any basic healing potions!\n")


		elif userInput == "Advanced Healing Potion":
			if DGPlayer.Inventory.advancedHealingPotion > 0:
				theResult = theResult + 1
				DGText.printScan(DGText.rip + "You used up 1 advanced healing potion")
				DGPlayer.Inventory.advancedHealingPotion = DGPlayer.Inventory.advancedHealingPotion - 1
				DGPlayer.heal(50)
				time.sleep(0.4)

			else:
				DGText.printScan(DGText.error + "You don't have any advanced healing potions!\n")


def usePoisonPotion():
	global DGPlayer
	theResult = 0
	if DGPlayer.Inventory.poisonPotion != 0:
		DGText.printScan(DGText.success + "You have {amount} poison potions."
		.format(amount=DGPlayer.Inventory.poisonPotion))

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
			if DGPlayer.Inventory.poisonPotion > 0:
				theResult = theResult + 1
				DGText.printScan(DGText.rip + "You used up 1 poison potion")
				DGPlayer.Inventory.poisonPotion = DGPlayer.Inventory.poisonPotion - 1
				time.sleep(0.4)

			else:
				DGText.printScan(DGText.error + "You don't have any poison potions!")
