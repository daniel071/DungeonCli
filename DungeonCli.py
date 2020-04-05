# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!
print("Welcome to DungeonCli!")

# Import Libraries here:
from colorama import init
init()
from colorama import Fore, Back, Style

# Define variables here:
# TODO: Add saving mechanic for these coins
coins = 0 # fucking poor cunt lmao.
success = Style.BRIGHT + Fore.GREEN + "==> "
rip = Style.BRIGHT + Fore.RED + "==> "


# Define functions here:

def checkCoins():
    global coins
    print("You have $" + str(coins) + "!")
    if coins == 0:
        print("You have 0 coins? I feel bad, here take 10 coins!")
        coins = coins + 10
        print(success + "10 coins have been added to your account. \n")


def main():
	command = input(Fore.CYAN + "Action> " + Style.RESET_ALL)
	if command in ("check money", "check coins", "coins", "c"):
		checkCoins()

# Run those functions here:
while True:
	main()
