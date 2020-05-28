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
