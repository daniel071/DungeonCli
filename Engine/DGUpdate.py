# Manages in-built updating of DungeonCli

import time
import os
from colorama import Fore, Back, Style
from colorama import init
from . import DGMain
from . import DGText

currentOS = DGMain.detect_system()

def check():
	print("Not completed yet, check back later!")

def update():
	if currentOS == "windows":
		DGText.printScan(DGText.rip + "Currently, only Linux and macOS support the automatic updater.\n")
	else:
		os.system("pwd")
		
		print("Updating...")
