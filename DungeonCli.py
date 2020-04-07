# DungeonCli is a terminal based program where you get to explore places and
# earn coins. You can spend those coins on various items, have fun!

# Import Libraries here:
import time
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
# This lad should heal about 20 HP
basicHealingPotion = 0

# Armour absorbs a percentage of damage, for example having copper armour
# absorbs 10% damage, so if you get 50 damage, you only get 45

# 0 = No Armour = 0% Absorbtion
# 1 = Copper Armour = 10% Absorbtion
# 2 = Iron Armour = 20% Absorbtion
# 3 = Platinum Armour = 30% Absorbtion
# 4 = Diamond Armour = 40% Absorbtion

armour = 0

# 1 x Matches.
# 3 x Sticks.
# (no sword)
# No healing potions
# No Armour

surroundingsLit = False
sceneOneCompleted = False

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
    print(success + "You have $" + str(coins) + "!")
    if coins == 0:
        print("You have 0 coins? I feel bad, here take 10 coins!")
        addCoins(10)


def openInventory():
	print(success + "Inventory:")
	count = 0
	if Matches != 0:
		print(str(Matches) + " x Matches")

	if Sticks != 0:
		print(str(Sticks) + " x Sticks")

	if basicHealingPotion != 0:
		print(str(basicHealingPotion) + " x Basic Healing Potion")

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
		print(rip + "You used up one match. \n")

	elif surroundingsLit == False:
		Matches = Matches - 1
		surroundingsLit = True
		print("You Light a match, your surroundings fill up with light. "
		"you can now see!")
		print(rip + "You used up one match. \n")


def start():
	global sceneOneCompleted

	if surroundingsLit == False:
		print("You find yourself in an odd and dark place... \nWhat could this"
		" possibly be?\n")
		time.sleep(2)

		print("Check your inventory, you might have something to \nimprove your vision...\n")
		time.sleep(2)
		#print("Maybe I should use a match to light this place up...") # too straight forward.

		#print(hint + "type 'm' to use a match)\n" + Style.RESET_ALL) # too straight forward.
	else:
		if sceneOneCompleted == False:
			print("This place looks like it's been abandoned decades ago...") # NOTE: describe this 'place'!
			print(action + "An odd creature begins to walk up to you... \n") # NOTE: describe this 'creature'! e.g. this oddly hunched over creature
			answer = ask("Should you hide or comfront them?", "h", "c")
			if answer == "c":
				# User selected comfront
				# Nothing special happens, it is passed on to the next part
				pass

			elif answer == "h":
				# User selected hide
				print(action + "You tried to hide, but there was nowhere to go, "
				"the figure began to comfront you.")
				time.sleep(3)

			print(action + "The odd figure got close enough until you "
			"could see it.") # NOTE: so is this a creature or figure
			time.sleep(2)

			print(action + "The figure looked like an ancient wizard. \n")
			time.sleep(2) #

			input(quote + 'Greetings, it seems you are new here,'
			' is that true?"\n' + Style.RESET_ALL)

			# NOTE: maybe. give the user a choice to say something.
			print(action + "You said yes. \n")
			time.sleep(0.7)

			print(quote + "I see, this is a dangerous place, so tread"
			' carefully..."') # ITS DANGEROUS TO GO ALONE.
			time.sleep(2)

			print(quote + 'Here, take this, it will help you defend yourself."')
			time.sleep(3) # TAKE THIS.

			print(success + "You recieved a basic sword.")
			print(success + "You recieved a basic healing potion.")
			addCoins(50)

			global Sword
			global basicHealingPotion

			basicHealingPotion = basicHealingPotion + 1
			Sword = 1
			sceneOneCompleted = True

		else:
			print(action + "You ask the ancient wizard:")
			time.sleep(1.7)

			print(Style.RESET_ALL + "Who are you?")
			time.sleep(1.2)
			print("What is this place? \n")
			time.sleep(1.2)

			print(action + "The wizard responds \n")
			time.sleep(1.7)

			print(quote + 'This place is an underground town, it used to be'
			' thriving, there were plenty of stores, lots of jobs, it was'
			' a great place to be...\n But then, the rebellion came in'
			' and wiped this place out, everybody either escaped or died.\n'
			' And me, I was the founder of this town." \n')
			time.sleep(10)

			input(quote + 'Would you like to recieve a quest?" \n'
			+ Style.RESET_ALL)
			print(action + "You said yes. \n")
			time.sleep(0.8)

			print(quote + 'Try and recover the Great Stone of Knowledge,'
			' it is located in the north-east room, however it is guarded'
			' by very powerful Almogates." \n')
			time.sleep(5)

			print(quote + 'Good luck." \n')
			time.sleep(2)

			print(action + "He leaves the room and now, you're on your own. \n")



def hpCheck():
	if hp != 100:
		print(success + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))
	elif hp == 100:
		print(success + "Your HP is maxed out!")


def main():
	command = input(Style.BRIGHT + Fore.CYAN + "[Action] " + Style.RESET_ALL)
	if command in ("check money", "check coins", "coins", "money", "c"):
		checkCoins()
	elif command in ("open inventory", "open inv" ,"inventory", "inv", "i","check inventory", "check inv"):
		openInventory()
	elif command in ("use match", "strike match", "match", "light match",
                    "use matches", "matches", "m"):
		useMatch()
	elif command in ("h", "help", "umm", "asdfghjkl", "qwertyuiop"):
		print("Help menu \n")

	elif command in ("e", "exit", "close", "alt-f4"):
		global mainLoop
		mainLoop = 0

	elif command in ("hp", "health", "health points"):
		hpCheck()

	elif command in ("s", "start", "observe","look around"):
		start()

# Introduce the user:
print("Welcome to " + Fore.GREEN + "DungeonCli!" + Style.RESET_ALL)
print("Type 'h' for help or 's' to start! \n")

# Run those functions here:
while mainLoop == 1:
	main()
