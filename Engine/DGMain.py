from colorama import Fore, Back, Style
from colorama import init
from sys import platform
import os
import time
from . import DGText
all_processes = []

def detect_system():
	global operatingsystem
	if platform == "linux" or platform == "linux2" or platform == "darwin":
		operatingsystem = "unix"
	else:
		operatingsystem = "windows"

detect_system()

def endThreads():
	for process in all_processes:
		process.stop()

def DGClear():
	if operatingsystem == "unix":
		_ = os.system('clear')
	else:
		_ = os.system('cls')

def EndScreen():
	print("exited game.")

def DGExit():
	global mainLoop
	print(Style.BRIGHT + Fore.YELLOW + "==> " + Style.RESET_ALL + "Closing DungeonCli...")
	time.sleep(0.2)
	DGText.printScan("See you next time.\n")
	time.sleep(0.5)
	DGClear()
	endThreads()
	mainLoop = 0
	EndScreen()
	os._exit(1)
