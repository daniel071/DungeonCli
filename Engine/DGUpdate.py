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
		DGText.printScan(DGText.loading + "Downloading new update (1/2)")
		print(Style.RESET_ALL)
		os.system("wget -O ./dungeoncli.zip https://git.pavela.net/attachments/9ba2e156-5732-4357-a641-269c25741f27")

		DGText.printScan(DGText.loading + "Extracting new update (2/2)")
		print(Style.RESET_ALL)
		os.system("unzip ./dungeoncli.zip -d ./dungeoncli/")

		DGText.printScan(DGText.success + "\nUpdate complete! Press enter to restart.")
		input("")
		DGMain.DGExit()
