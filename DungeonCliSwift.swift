
// Define variables here:

//TODO: Add saving mechanic for these coins
var mainLoop = 1
var coins = 0 // fucking poor cunt lmao.
var hp = 100
// Events used for random stuff:
var events = ["store", "randomFight"]

// Inventory
var Matches = 1
var Sticks = 3
var Sword = 0
// This lad should heal about 20 HP
var basicHealingPotion = 0

// Armour absorbs a percentage of damage, for example having copper armour
// absorbs 10% damage, so if you get 50 damage, you only get 45

// 0 = No Armour = 0% Absorbtion
// 1 = Copper Armour = 10% Absorbtion
// 2 = Iron Armour = 20% Absorbtion
// 3 = Platinum Armour = 30% Absorbtion
// 4 = Diamond Armour = 40% Absorbtion

var armour = 0
var bsorbtion = 0 // Out of 100%
var damageMultiplyer = 1
var CSDescription = "You haven't started yet!" // description of current room, called by observe and look around

// 1 x Matches.
// 3 x Sticks.
// (no sword)
// No healing potions
// No Armour

var surroundingsLit = false
var currentScene = 1

struct Fore {
    var YELLOW = "\u{001B}[0;33m"
}

var success = Fore.GREEN + "==> "
var rip = Fore.RED + "==> "
var question = Fore.YELLOW + "[?] "
var error = Fore.RED + "[!] "
var hint = Fore.WHITE + "(hint: "
var action = Fore.YELLOW + "==> "
var quote = Fore.WHITE + '"'


var coinsInScene = false

/// Define functions here:

//Some useful stuff

/*
func removeFromList(list, removal) {
	index = 0
	listLoop = True
    while listLoop {
        if list[index] == removal {
			modifiedList = list
			modifiedList.pop(index)

			return modifiedList
			listLoop = False

        } else {
			index = index + 1
        }
    }
}
*/

/*
def detect_system():
    global operatingsystem
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        operatingsystem = "unix"
*/

def clear():
    if operatingsystem == "unix":
        _= os.system('clear')
    else:
        _= os.system('cls')


def isDead():
	if hp < 0:
		gameover()


def gameover():
	clear()
	print(rip + "Your body is torn into shreads...")
	time.sleep(4)
	print(Style.BRIGHT + Fore.YELLOW + ".")
	time.sleep(1.5)
	print("..")
	time.sleep(1.5)
	print("...\n")
	time.sleep(1.5)

	print(Style.BRIGHT + Fore.RED + "Game Over!")
	time.sleep(2)

	print(Style.BRIGHT + Fore.WHITE + "Maybe next time, you might be lucky...\n")
	time.sleep(5)
	clear()
	exit()


def addCoins(add):
    global coins
    coins = coins + add
    print(success + ("You pocketed " + str(add) + " coins! \n"))


def removeCoins(value):
    global coins
    coins = coins - value
    print(rip + ("You dropped " + str(value) + " coins! \n"))


def spendCoins(value):
	global coins
	coins = coins + value
	print(success + ("You spent " + str(value) + " coins! \n"))


def ask(funcQuestion, answer1, answer2):
	askLoop = 1
	while askLoop == 1:
		// Asks the user a question
		userInput = input(question + "{funcQuestion} [{answer1}/{answer2}] "
		.format(funcQuestion=funcQuestion, answer1=answer1, answer2=answer2)
		 + Style.RESET_ALL)

		// Checks if it's correct
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


def damage(value):
	global hp
	hp = hp - value
	print(rip + ("You lost " + str(value) + " health! \n"))
	isDead()

def heal(value):
	global hp
	hp = hp + value
	print(success + ("You gained " + str(value) + " health! \n"))


def combat(enemy, enemyHP):
	global hp
	print(rip + "You get in a battle with {enemy}!\n".format(enemy=enemy))
	time.sleep(1)

	combatLoop = True
	while combatLoop:
		time.sleep(1)

		userInput = ask("Fight or Flee?", "fight", "flee")
		if userInput == "fight":
			// Calculates damage
			damage = random.randint(5, 10) * damageMultiplyer
			enemyDamage = random.randint(5, 10)

			// Applies damage
			hp = hp - enemyDamage
			enemyHP = enemyHP - damage

			// Displays to user
			print(success + "You deal {damage} damage!".format(damage=damage))
			print(rip + "{name} deals {damage} damage!\n".format(damage=enemyDamage, name=enemy))
			time.sleep(1)
			isDead()

			if enemyHP < 0:
				print(success + "You successfully killed {name}\n".format(name=enemy))
				time.sleep(1)
				extraCoins = random.randint(10, 25)
				addCoins(extraCoins)
				combatLoop = False
				return "kill"


		elif userInput == "flee":
			chance = random.randint(1, 2)
			if chance == 1:
				print(action + "You run away before {name} could catch you.\n".format(name=enemy))
				combatLoop = 0
				time.sleep(1)

				return "flee"

			elif chance == 2:
				print(action + "You tried to flee, but {name} caught you. \n".format(name=enemy))
				time.sleep(1.5)

				enemyDamage = random.randint(10, 20)
				hp = hp - enemyDamage
				print(rip + "{name} deals {damage} damage!\n".format(damage=enemyDamage, name=enemy))
				time.sleep(1)
				isDead()


//// Commands used

def checkCoins():
	global coins
	print(success + "You have $" + str(coins) + "!\n")
	if coins == 0:
		time.sleep(1)
		print(Style.BRIGHT + Fore.WHITE + "You have 0 coins? I feel bad, here"
		" take 10 coins!")
		time.sleep(2)
		addCoins(10)
		time.sleep(1)


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
		// TODO: Implement more then just a basic sword.
		print("Basic Sword")

	// This print just adds some white space
	print(" ")


def useMatch():
	global Matches
	global surroundingsLit
	global CSDescription

	if Matches == 0:
		print(error + "You don't have any matches!\n")
	elif surroundingsLit == True:
		Matches = Matches - 1
		print("You light a match. it begins to burn away.")
		print(rip + "You used up one match. \n")

	elif surroundingsLit == False:
		CSDescription = "This place is in ruins, possibly for decades."

		Matches = Matches - 1
		surroundingsLit = True
		print("You Light a match, your surroundings fill up with light. "
		"you can now see!")
		print(rip + "You used up one match. \n")


def start():
	global CSDescription
	global coinsInScene
	global currentScene

	if surroundingsLit == False:
		print("You find yourself in an odd and dark place... \nWhat could this"
		" possibly be?\n")
		CSDescription = "This place is extremely dark, you can't see anything..."
		time.sleep(2)

		print("Check your inventory, you might have something to \nimprove your vision...\n")
		time.sleep(2)
		// combat("Bob", 69)
		//print("Maybe I should use a match to light this place up...") // too straight forward.

		//print(hint + "type 'm' to use a match)\n" + Style.RESET_ALL) // too straight forward.
	else:
		if currentScene == 1:
			print("This place looks like it's been abandoned decades ago...") // NOTE: describe this 'place'!
			print(action + "An odd creature begins to walk up to you... \n") // NOTE: describe this 'creature'! e.g. this oddly hunched over creature
			answer = ask("Should you hide or comfront them?", "h", "c")
			if answer == "c":
				// User selected comfront
				// Nothing special happens, it is passed on to the next part
				pass

			elif answer == "h":
				// User selected hide
				print(action + "You tried to hide, but there was nowhere to go, "
				"the figure began to comfront you.")
				time.sleep(3)

			print(action + "The odd figure got close enough until you "
			"could see it.") // NOTE: so is this a creature or figure
			time.sleep(2)

			print(action + "The figure looked like an ancient wizard. \n")
			time.sleep(2) //

			input(quote + 'Greetings, it seems you are new here,'
			' is that true?"\n' + Style.RESET_ALL)

			// NOTE: maybe. give the user a choice to say something.
			print(action + "You said yes. \n")
			time.sleep(0.7)

			print(quote + "I see, this is a dangerous place, so tread"
			' carefully..."') // ITS DANGEROUS TO GO ALONE.
			time.sleep(2)

			print(quote + 'Here, take this, it will help you defend yourself."')
			time.sleep(3) // TAKE THIS.

			print(success + "You recieved a basic sword.")
			print(success + "You recieved a basic healing potion.")
			addCoins(50)

			global Sword
			global basicHealingPotion

			basicHealingPotion = basicHealingPotion + 1
			Sword = 1
			currentScene = 2

		elif currentScene == 2:
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
			CSDescription = "This place is in ruins, apparently it's supposed to be a town...\nThere is a door to the next room, something seems to be strung across it."

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
			currentScene = 3

		elif currentScene == 3:
			CSDescription = "The room looked very charred after the explosion."

			print(action + "After the wizard left, you went into the next room. \n")
			time.sleep(2)

			print(action + "It is odly quiet here... you begin to look around... \n")
			time.sleep(3)

			print(rip + "BANG! A small bomb exploded, it was a trap!")
			damage(20)
			time.sleep(2)
			currentScene = 4

		elif currentScene == 4:
			print(action + "You proceed to the next room, being very careful where you step.")

			CSDescription = "This room is rather empty, but an old and dried up fountain lays ahead.\na few coins lay scattered across the bottom, maybe you can pick them up..."
			coinsInScene = True
			time.sleep(2)

			print(action + "You quickly hear a movement and freeze...\n")
			time.sleep(2)

			print(quote + 'IT WAS YOU WHO DID IT! Y-YOU WERE THE ONE WHO KILLED ALL M'
			'-MY F-F-FRIENDS!"\n')
			time.sleep(3)
			print(action + "You try to explain that they were mistaken but"
			" it was too late. \n")
			time.sleep(2)


			theResult = combat("Unidentified", 25)
			if theResult == "kill":
				print(action + "You killed the unknown person however, you can't stop feeling bad. \n")

			elif theResult == "flee":
				print(action + "You quickly ran away, you're safe now. \n")

			currentScene = 5

		elif currentScene == 5:
			// It is done bois!
			randomEvent()


def hpCheck():
	// Displays different colour depending on hp

	if hp > 70:
		print(success + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))

	elif hp > 35:
		print(action + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))

	else:
		print(rip + "You have {hp} out of {max} HP! \n".format(hp=hp, max=100))


def randomEvent():
	print("This is a randomly generated event! The stories in here have not been completed yet.")

	global events
	randomLoop = True

	if len(events) > 0:
		selection = random.choice(events)
		if selection == "store":
			print("Store selected")

		elif selection == "randomFight":
			print("randomFight selected")

		events = removeFromList(events, selection)

	else:
		print("There are no more unvisited events left!")

def lookAround():
	print(CSDescription + "\n")


def pickCoins():
	global coinsInScene

	if coinsInScene == True:
		amount = random.randint(4, 6)
		print(action + "You reach down and pick up all the coins from the floor.")
		time.sleep(1)

		addCoins(amount)
		coinsInScene = False


	else:
		print(error + "There are no coins to pick up! \n")


def main():
	detect_system()

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

	elif command in ("s", "start", "next", "proceed", "next room", "forth"):
		start()

	elif command in ("l", "look around", "look", "observe"):
		lookAround()


	if command in ("pickup coins", "pick up coins", "pick coins"):
		pickCoins()


// Introduce the user:
print("Welcome to " + Fore.GREEN + "DungeonCli!" + Style.RESET_ALL)
print("Type 'h' for help or 's' to start! \n")

// Run those functions here:
while mainLoop == 1:
	main()