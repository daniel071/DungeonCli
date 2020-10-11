from pypresence import Presence
from colorama import Fore, Back, Style
from colorama import init
import sys
import time

client_id = '714997150941053028'  # Yes, this is our ID.
error = Style.BRIGHT + Fore.RED + "[!] "

try:
	RPC = Presence(client_id)  # Initialize the client class
	RPC.connect() # Start the handshake loop
except:
	pass

def init():
	try:
		RPC.update(state="Scene 0", details="A terminal-based dungeon game!", large_text="git.pavela.net/Daniel/DungeonCli", large_image="epicterminal")  # Set the presence
	except:
		if "-debug" in sys.argv:
			print(error + "There was an error while starting discord rich presence.")
			print(Fore.WHITE + Style.BRIGHT + "Make sure you have discord open.")
			time.sleep(1)
		else:
			print(" ")

def present(sceneNumber):
	try:
		global RPC
		RPC.update(large_image="epicterminal", state="Scene {scene}".format(scene=sceneNumber), details="A terminal-based dungeon game!", large_text="git.pavela.net/Daniel/DungeonCli",)  # Set the presence
	except:
		pass
