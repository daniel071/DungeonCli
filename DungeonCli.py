# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!
print("Welcome to DungeonCli!")

# Import Libraries here:
from colorama import init
init()
from colorama import Fore, Back, Style

# Define variables here:
## TODO: Add saving mechanic for these coins
mainLoop = 1
coins = 0 # fucking poor cunt lmao.
hp = 100

Matches = 1
Sticks = 3
Sword = 0
# 1 x Matches.
# 3 x Sticks.
# (no sword)

surroundingsLit = False


success = Style.BRIGHT + Fore.GREEN + "==> "
rip = Style.BRIGHT + Fore.RED + "==> "
question = Style.BRIGHT + Fore.YELLOW + "[?] "
error = Style.BRIGHT + Fore.RED + "[!] "

# Define functions here:

## Some useful stuff

def addCoins(add):
    global coins
    coins = coins + add
    print(success + ("You pocketed " + str(add) + " coins! \n"))


def removeCoins(value):
    global coins
    coins = coins - value
    print(rip + ("You dropped " + str(value) + " coins! \n"))


def spendCoins(value):
    print(success + ("You spent " + str(value) + " coins! \n"))

## Commands used

def checkCoins():
    global coins
    print("You have $" + str(coins) + "!")
    if coins == 0:
        print("You have 0 coins? I feel bad, here take 10 coins!")
        removeCoins(10)
        addCoins(69)


def openInventory():
	print(success + "Inventory:")
	count = 0
	if Matches != 0:
		print(str(Matches) + " x Matches")

	if Sticks != 0:
		print(str(Sticks) + " x Sticks")

	if Sword != 0:
		# TODO: Implement more then just a basic sword.
		print("Basic Sword")

	# This print just adds some white space
	print(" ")


def useMatch():
	global Matches
	global surroundingsLit
	if Matches == 0:
		print(error + "You don't have any matches!\n")
	elif surroundingsLit == True:
		Matches = Matches - 1
		print("You Light a match. it begins to burn away.")
		print(rip + "You used up one match \n")

	elif surroundingsLit == False:
		Matches = Matches - 1
		surroundingsLit = True
		print("You Light a match, your surroundings fill up with light. "
		"you can now see!")
		print(rip + "You used up one match \n")


def hpCheck():
	print(success + "You have {hp} out of {max} hp! \n".format(hp=hp, max=100))

def main():
	command = input(Style.BRIGHT + Fore.CYAN + "[Action] " + Style.RESET_ALL)
	if command in ("check money", "check coins", "coins", "c"):
		checkCoins()
	elif command in ("open inventory", "open inv" ,"inventory", "inv", "i"):
		openInventory()
	elif command in ("use match", "strike match", "match", "light match",
                    "use matches", "matches", "m"):
		useMatch()
	elif command in ("h", "help"):
		print("Help menu \n")

	elif command in ("e", "exit"):
		global mainLoop
		mainLoop = 0

	elif command in ("h", "hp"):
		hpCheck()


# Run those functions here:
while mainLoop == 1:
	main()
