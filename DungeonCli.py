# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!

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
hint = Style.DIM + Fore.WHITE + "(hint: "
action = Style.BRIGHT + Fore.YELLOW + "==> "
quote = Style.BRIGHT + Fore.WHITE + '"'

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


def ask(funcQuestion, answer1, answer2):
	askLoop = 1
	while askLoop == 1:
		# Asks the user a question
		userInput = input(question + "{funcQuestion} [{answer1}/{answer2}] "
		.format(funcQuestion=funcQuestion, answer1=answer1, answer2=answer2)
		 + Style.RESET_ALL)

		# Checks if it's correct
		if userInput == answer1:
			askLoop = 0
			print("")
			return answer1
		elif userInput == answer2:
			askLoop = 0
			print("")
			return answer2
		else:
			print(error + "Answer must be either "
			"{answer1} or {answer2}!\n".format(answer1=answer1, answer2=answer2))


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
		print("You light a match. it begins to burn away.")
		print(rip + "You used up one match \n")

	elif surroundingsLit == False:
		Matches = Matches - 1
		surroundingsLit = True
		print("You Light a match, your surroundings fill up with light. "
		"you can now see!")
		print(rip + "You used up one match. \n")


def start():
	if surroundingsLit == False:
		print("You find yourself in an odd, dark place... \nWhat could this"
		" possibbly be?")
		print("Maybe I should use a match to light this place up...")
		print(hint + "type 'm' to use a match)\n" + Style.RESET_ALL)
	else:
		print("Wow, this place looks like it's been abandoned decades ago...")
		print(action + "An odd creature begins to walk up to you... \n")
		answer = ask("Should you hide or comfront them?", "h", "c")
		if answer == "c":
			# TODO: Add sleep function so it doesn't show up all at once!
			# User selected comfront
			print(action + "The odd figure got close enough until you"
			"could see it.")
			print(action + "The figure looked like an ancient wizard. \n")

			input(quote + 'Greetings, it seems you are new here,'
			' is that true?"\n')
			print(action + "You said yes.")
			print(quote + "I see, this is a dangerous place, so tread"
			' carefully..."')
			print(quote + 'Here, take this, it will help you defend yourself."')
			print(success + "You recieved a basic sword.")
			global Sword
			Sword = 1


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

	elif command in ("hp", "health"):
		hpCheck()

	elif command in ("s", "start", "observe"):
		start()

# Introduce the user:
print("Welcome to " + Fore.GREEN + "DungeonCli!" + Style.RESET_ALL)
print("Type 'h' for help, 's' to start! \n")

# Run those functions here:
while mainLoop == 1:
	main()
