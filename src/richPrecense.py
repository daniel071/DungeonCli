from pypresence import Presence
import time

import DungeonCli
sceneNumber = 12

client_id = '714997150941053028'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

RPC.update(state="Scene {scene}".format(scene=sceneNumber), details="A terminal-based dungeon crawler game!", large_text="pavela.net:3000/Daniel/DungeonCli", large_image="epicTerminal.png")  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
