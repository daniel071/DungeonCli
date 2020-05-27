from pypresence import Presence
import time

client_id = '714997150941053028'  # Fake ID, put your real one here

def init():
	RPC = Presence(client_id)  # Initialize the client class
	RPC.connect() # Start the handshake loop
		RPC.update(state="Scene 0", details="A terminal-based dungeon crawler game!", large_text="pavela.net:3000/Daniel/DungeonCli", large_image="epicTerminal.png")  # Set the presence

def present(sceneNumber):
	RPC.update(state="Scene {scene}".format(scene=sceneNumber), details="A terminal-based dungeon crawler game!", large_text="pavela.net:3000/Daniel/DungeonCli", 		large_image="epicTerminal.png")  # Set the presence
