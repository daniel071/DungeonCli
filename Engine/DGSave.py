from . import DGText
from . import DGScene
from . import DGPlayer
from PyInquirer import prompt, print_json
from colorama import Fore, Back, Style
from colorama import init
import time
import json
import jsonpickle

# FIXME: Save system is a buggy mess

def save():
	# TODO: Make the save function actually work
	questions = [
		{

			'type': 'input',
			'message': 'What is the file that you would like to save in?',
			'name': 'location'
		}
	]
	answers = prompt(questions)
	userInput = answers['location']

	print(userInput)


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
	userInput = answers['location']

	print(userInput)

	with open(directory, 'r', encoding='utf-8') as f:
		saveFile = json.load(f)
