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
	# TODO: Convert this to PyInquirer
	DGText.printScan(DGText.hint + "For example, '/home/user/save.json')")
	directory = input(Style.RESET_ALL + DGText.question + "What is the file that you would "
					  "like to save in? ")

	for variable in iojsfdiosjf


def load():
	pass
