# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!
print("Hello World")

coins = 0 # fucking poor cunt lmao.


# Import Libraries here:



# Define functions here:

def checkCoins():
	print("you have $" + str(coins) + "!")

def main():
	x = input("Action> ")
	if x in ("check money", "check coins"):
		checkCoins()

# Run those functions here:
while True:
	main()