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
		"DGPlayer": {
			"coins": DGPlayer.coins,
			"hp": DGPlayer.hp,
			"moneyMultiplyer": DGPlayer.Inventory.moneyMultiplyer,
			"matches": DGPlayer.Inventory.matches,
			"sticks": DGPlayer.Inventory.sticks,
			"basicHealingPotion": DGPlayer.Inventory.basicHealingPotion,
			"advancedHealingPotion": DGPlayer.Inventory.advancedHealingPotion,
			"poisonPotion": DGPlayer.Inventory.poisonPotion,
			"sword": DGPlayer.Inventory.sword,
			"damage": DGPlayer.Inventory.damage,
			"armour": DGPlayer.Inventory.armour,
			"absorbtion": DGPlayer.Inventory.absorbtion,
			"secretKey": DGPlayer.Inventory.secretKey,
		},
		"DGScene": {
			"canProgress": DGScene.canProgress,
			"current": DGScene.current,
			"surroundingsLit": DGScene.surroundingsLit,
			"hasStore": DGScene.hasStore,
			"hasCoins": DGScene.hasCoins,
			"hasVault": DGScene.hasVault,
			"description": DGScene.description,
			"soundDescription": DGScene.soundDescription,
		}
	}

	with open(directory, 'w', encoding='utf-8') as f:
		json.dump(saveFile, f, ensure_ascii=False, indent=4)

	DGText.printScan(DGText.success + "Successfully saved to {dir}!\n".format(dir=directory))


def load():
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

	for i in saveFile:
		print(i)
