# Manages in-built updating of DungeonCli
# TODO: Improve to include update checks, nightly and stable updates and windows&mac support
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
	elif currentOS == "darwin":
		DGText.printScan(DGText.rip + "macOS support is coming soon.\n")
	else:
		DGText.printScan(DGText.loading + "Downloading new update (1/2)")
		print(Style.RESET_ALL)
		os.system("wget -O ./dungeoncli.zip https://github.com/daniel071/DungeonCli/releases/download/v0.6.0-beta/DungeonCli-linux.zip")

		DGText.printScan(DGText.loading + "Extracting new update (2/2)")
		print(Style.RESET_ALL)
		os.system("unzip ./dungeoncli.zip -d ./dungeoncli/")

		DGText.printScan(DGText.success + "\nUpdate complete! Press enter to restart.")
		input("")
		DGMain.DGExit()
