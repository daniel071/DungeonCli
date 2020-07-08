from . import DGText
from . import DGScene
from . import DGPlayer
from PyInquirer import prompt, print_json
from colorama import Fore, Back, Style
from colorama import init
import time
import json
import inspect


def save():
	questions = [
		{

			'type': 'input',
			'message': 'What is the file that you would like to save in?',
			'name': 'location'
		}
	]
	answers = prompt(questions)
	directory = answers['location']

	saveFile = {
		# Put values in Engine/DGPlayer.py
		"DGPlayer.coins": DGPlayer.coins,
		"DGPlayer.hp": DGPlayer.hp,
		"DGPlayer.Inventory.moneyMultiplyer": DGPlayer.Inventory.moneyMultiplyer,
		"DGPlayer.Inventory.matches": DGPlayer.Inventory.matches,
		"DGPlayer.Inventory.sticks": DGPlayer.Inventory.sticks,
		"DGPlayer.Inventory.basicHealingPotion": DGPlayer.Inventory.basicHealingPotion,
		"DGPlayer.Inventory.advancedHealingPotion": DGPlayer.Inventory.advancedHealingPotion,
		"DGPlayer.Inventory.poisonPotion": DGPlayer.Inventory.poisonPotion,
		"DGPlayer.Inventory.sword": DGPlayer.Inventory.sword,
		"DGPlayer.Inventory.damage": DGPlayer.Inventory.damage,
		"DGPlayer.Inventory.armour": DGPlayer.Inventory.armour,
		"DGPlayer.Inventory.absorbtion": DGPlayer.Inventory.absorbtion,
		"DGPlayer.Inventory.secretKey": DGPlayer.Inventory.secretKey,

		# Put values in Engine/DGScene.py
		"DGScene.canProgress": DGScene.canProgress,
		"DGScene.current": DGScene.current,
		"DGScene.surroundingsLit": DGScene.surroundingsLit,
		"DGScene.hasStore": DGScene.hasStore,
		"DGScene.hasCoins": DGScene.hasCoins,
		"DGScene.hasVault": DGScene.hasVault,
		"DGScene.description": DGScene.description,
		"DGScene.soundDescription": DGScene.soundDescription,
	}

	with open(directory, 'w', encoding='utf-8') as f:
		json.dump(saveFile, f, ensure_ascii=False, indent=4)

	DGText.printScan(DGText.success + "Successfully saved to {dir}!\n".format(dir=directory))


def load():
	global DGPlayer
	global DGScene
	# TODO: Make the load function actually work

	questions = [
		{

			'type': 'input',
			'message': 'What is the directory the save file is in?',
			'name': 'location'
		}
	]
	answers = prompt(questions)
	directory = answers['location']

	with open(directory, 'r', encoding='utf-8') as f:
		saveFile = json.load(f)

	for key, value in saveFile.items():
		print(key)
		print(value)

		exec(key, "=", value)
