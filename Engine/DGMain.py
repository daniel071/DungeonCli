# Some common functions that are used

from colorama import Fore, Back, Style
from colorama import init
from sys import platform
import os
import time
import simpleaudio
from simpleaudio import _simpleaudio
from pydub import generators
from pydub.playback import _play_with_simpleaudio
import pydub
from . import DGText
from . import DGMain
from . import DGPlayer

playMusic = True
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

def playSound(path, ifLoop):
	global all_process
	if DGMain.playMusic == True:
		if ifLoop is True:
			playback = _play_with_simpleaudio(pydub.AudioSegment.from_ogg(path) * 20)
		else:
			playback = _play_with_simpleaudio(pydub.AudioSegment.from_ogg(path))

		all_processes.append(playback)
	else:
		return "No music played"

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

def isDead():
	if DGPlayer.hp < 0:
		gameover()

def hpCheck():
	# Displays different colour depending on hp
	global DGPlayer
	if DGPlayer.hp > 100:
		DGPlayer.hp = 100

	DGPlayer.hp = round(DGPlayer.hp)

	if DGPlayer.hp > 70:
		DGText.printScan(
			DGText.success + "You have {hp} out of {max} HP! \n".format(hp=DGPlayer.hp, max=100))

	elif DGPlayer.hp > 35:
		DGText.printScan(
			DGText.action + "You have {hp} out of {max} HP! \n".format(hp=DGPlayer.hp, max=100))

	else:
		DGText.printScan(rip + "You have {hp} out of {max} HP! \n".format(hp=DGPlayer.hp, max=100))

def addCoins(add):
	global DGPLayer
	DGPlayer.coins = DGPlayer.coins + add
	DGText.printScan(DGText.success + ("You pocketed " + str(add) + " coins! \n"))


def removeCoins(value):
	global DGPlayer
	DGPlayer.coins = DGPlayer.coins - value
	DGText.printScan(DGText.rip + ("You dropped " + str(value) + " coins! \n"))


def spendCoins(value):
	global DGPlayer
	DGPlayer.coins = DGPlayer.coins + value
	DGText.printScan(DGText.success + ("You spent " + str(value) + " coins! \n"))
