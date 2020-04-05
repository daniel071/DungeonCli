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


def main():
	command = input(Fore.CYAN + "[Action] " + Style.RESET_ALL)
	if command in ("check money", "check coins", "coins", "c"):
		checkCoins()

	elif command in ("h", "help"):
		print("Help menu \n")

	elif command in ("e", "exit"):
		global mainLoop
		mainLoop = 0


# Run those functions here:
while mainLoop == 1:
	main()
