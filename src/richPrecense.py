from pypresence import Presence
import time

client_id = '714997150941053028'  # Fake ID, put your real one here

try:
	RPC = Presence(client_id)  # Initialize the client class
	RPC.connect() # Start the handshake loop
except:
	print("warning: discord isn't running or missing package?")

def init():
	try:
		RPC.update(state="Scene 0", details="A terminal-based dungeon game!", large_text="pavela.net:3000/Daniel/DungeonCli", large_image="epicterminal")  # Set the presence
	except:
		print("warning: discord isn't running or missing package?")
def present(sceneNumber):
	try:
		global RPC
		RPC.update(large_image="epicterminal", state="Scene {scene}".format(scene=sceneNumber), details="A terminal-based dungeon game!", large_text="pavela.net:3000/Daniel/DungeonCli",)  # Set the presence
	except:
		pass
