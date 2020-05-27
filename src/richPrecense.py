from pypresence import Presence
import time

client_id = '714997150941053028'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

def init():
	RPC.update(state="Scene 0", details="A terminal-based dungeon game!", large_text="pavela.net:3000/Daniel/DungeonCli", large_image="epicterminal")  # Set the presence

def present(sceneNumber):
	global RPC
	RPC.update(large_image="epicterminal", state="Scene {scene}".format(scene=sceneNumber), details="A terminal-based dungeon game!", large_text="pavela.net:3000/Daniel/DungeonCli",)  # Set the presence
