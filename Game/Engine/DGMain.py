# Some common functions that are used
# Usually we just dump stuff here that are related to the main function of
# the engine

from colorama import Fore, Back, Style
from colorama import init
from sys import platform
import os
import time
import simpleaudio
import sys
from simpleaudio import _simpleaudio
from pydub import generators
from pydub.playback import _play_with_simpleaudio
import pydub
from . import DGText
from . import DGMain
from . import DGPlayer
from . import DGDialog
from . import DGScene

playMusic = True
soundPlaying = True
all_processes = []

def detect_system():
	global operatingsystem
	if platform == "linux" or platform == "linux2":
		return "linux"
	elif platform == "darin":
		return "darwin"
	elif platfrom == "windows":
		return "windows"
	else:
		return "nerd"

operatingsystem = detect_system()

def endThreads():
	for process in all_processes:
		process.stop()

def DGClear():
	if operatingsystem == "linux" or operatingsystem == "darwin":
		_ = os.system('clear')
	else:
		_ = os.system('cls')

def EndScreen():
	print("exited game.")

def playSound(path, ifLoop):
	global all_process
	if "-mute" not in sys.argv:
		if DGMain.playMusic == True:
			if ifLoop is True:
				playback = _play_with_simpleaudio(pydub.AudioSegment.from_ogg(path) * 20)
			else:
				playback = _play_with_simpleaudio(pydub.AudioSegment.from_ogg(path))

			all_processes.append(playback)
		else:
			return "No music played"

def toggleSound():
	global playMusic

	playMusic = not playMusic
	if playMusic is False:
		disableSound()
	else:
		enableSound()

def enableSound():
	# Currently does not account for scene 0 and scene 1, will be fixed in
	# a future sound update

	global soundPlaying
	if soundPlaying == False:
		if DGScene.current > 2:
			DGMain.playSound("Music/quest.ogg", True)
		else:
			DGMain.playSound("Music/intro.ogg", True)
		soundPlaying = True

def disableSound():
	global soundPlaying
	endThreads()
	soundPlaying = False


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
		DGText.printScan(DGText.rip + "You have {hp} out of {max} HP! \n".format(hp=DGPlayer.hp, max=100))

def addCoins(add):
	DGMain.playSound("Sounds/coin.ogg", False)

	global DGPLayer
	toAdd = add * DGPlayer.Inventory.moneyMultiplyer

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


def gameover():
	endThreads()
	DGMain.playSound("Music/gameOver.ogg", False)
	DGMain.DGClear()
	DGText.printScan(DGText.rip + "Your body is torn into shreads...")
	time.sleep(2)
	DGText.printScan(Style.BRIGHT + Fore.YELLOW + ".")
	time.sleep(1)
	DGText.printScan("..")
	time.sleep(1)
	DGText.printScan("...\n")
	time.sleep(1)

	DGText.printScan(Style.BRIGHT + Fore.WHITE +

		  "   _____					   _\n"
		  " / ____|					  | |\n"
		  "| |  __  __ _ _ __ ___   ___	_____   _____ _ __| |\n"
		  "| | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__| |\n"
		  "| |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |  |_|\n"
		  " \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|  (_)\n"
		  )

	time.sleep(2)

	DGText.printScan(Style.BRIGHT + Fore.WHITE +
		  DGDialog.randomDialog.gameoverText())
	time.sleep(5.5)
	DGClear()
	endThreads()
	os._exit(1)
