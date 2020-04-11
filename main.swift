import Foundation
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


// \u{001B}[\(attribute code like bold, dim, normal);\(color code)m

// Color codes
// black   30
// red     31
// green   32
// yellow  33
// blue    34
// magenta 35
// cyan    36
// white   37

var DIM = "\u{001B}[2m"
var BOLD = "\u{001B}[1m"
var BLACK = "\u{001B}[0;30m"
var BOLDBLACK = "\u{001B}[0;30m"
var RED = "\u{001B}[0;31m"
var GREEN = "\u{001B}[0;32m"
var YELLOW = "\u{001B}[0;33m"
var BLUE = "\u{001B}[0;34m"
var MAGENTA = "\u{001B}[0;35m"
var CYAN = "\u{001B}[0;36m"
var WHITE = "\u{001B}[0;37m"
var GRAY = "\u{001B}[2;37m"
var RESETCLR = "\u{001B}[0;00m"


var success = BOLD + GREEN + "==> "
var rip = BOLD + RED + "==> "
var question = BOLD + YELLOW + "[?] "
var error = BOLD + RED + "[!] "
var hint = DIM + GRAY + "(hint: "
var action = BOLD + YELLOW + "==> "
var quote = BOLD + WHITE + "\""


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



func isDead() {
	if hp < 0 {
		gameover()
	}
}

func gameover() {
	print(rip + "Your body is torn into shreads...")
	sleep(4)
	print(YELLOW + ".")
	sleep(1)
	print("..")
	sleep(1)
	print("...\n")
	sleep(1)

	print(RED + "Game Over!")
	sleep(2)

	print(WHITE + "Maybe next time, you might be lucky...\n")
	sleep(5)
	//clear()
	//exit()

}


func addCoins(value: Int) {
	coins = coins + value
	print(success + ("You pocketed " + String(value) + " coins! \n"))
}


func removeCoins(value: Int) {
	coins = coins - value
	print(rip + ("You dropped " + String(value) + " coins! \n"))
}


func spendCoins(value: Int) {
	coins = coins + value
	print(success + ("You spent " + String(value) + " coins! \n"))
}


func ask(funcQuestion: String, answer1: String, answer2: String) -> String {
	var askLoop = 1
	while askLoop == 1 {
		// Asks the user a question
		print (question + funcQuestion + " [" + answer1 + "/" + answer2 + "]", terminator:"")
		let userInput = readLine()

		// Checks if it's correct

		if userInput == answer1 {
			askLoop = 0
			print("")
			return answer1
		} else if userInput == answer2 {
			askLoop = 0
			print("")
			return answer2
		} else {
			print(error + "Answer must be either " + answer1 + " or " + answer2 + "!")
		}
	}
}



func damage(value: Int) {
	hp = hp - value
	print(rip + ("You lost " + String(value) + " health!"))
	isDead()
}

func heal(value: Int) {
	hp = hp + value
	print(success + ("You gained " + String(value) + " health!"))
}

func combat(enemy: String, enemyHP: Int) -> String {

	var currentEnemyHP = enemyHP
	print(rip + "You get in a battle with " + enemy + "!\n")
	sleep(1)

	var combatLoop = true
	repeat {
		sleep(1)

		let userInput = ask(funcQuestion: "Fight or Flee?", answer1: "fight", answer2: "flee")
		if userInput == "fight" {
			// Calculates damage
			let selfDamage = Int.random(in: 5..<10) * damageMultiplyer
			let enemyDamage = Int.random(in: 5..<10)

			// Applies damage
			hp = hp - enemyDamage
			currentEnemyHP = currentEnemyHP - selfDamage

			// Displays to user
			print(success + "You deal " + String(selfDamage) + " damage!" + WHITE)
			print(rip + enemy + " deals " + String(enemyDamage) + " damage!" + WHITE)
			sleep(1)
			isDead()

			if enemyHP < 0 {
				print(success + "You successfully killed " + enemy + WHITE)
				sleep(1)
				let extraCoins = Int.random(in: 10..<25)
				addCoins(value: extraCoins)
				combatLoop = false
				return "kill"
			}

		} else if userInput == "flee" {
			let chance = Int.random(in: 1..<2)
			if chance == 1 {
				print(action + "You run away before " + enemy + " could catch you" + WHITE)
				combatLoop = false
				sleep(1)

				return "flee"

			} else if chance == 2 {
				print(action + "You tried to flee, but " + enemy + " caught you." + WHITE)
				sleep(1)

				let enemyDamage = Int.random(in: 10..<20)
				hp = hp - enemyDamage
				print(rip + enemy + " deals " + String(enemyDamage) + " damage!" + WHITE)
				sleep(1)
				isDead()
			}
		}
	} while combatLoop
}
/// Commands used

func checkCoins() {
	print(success + "You have $" + String(coins) + "!\n")
	if coins == 0 {
		sleep(1)
		print(WHITE + "You have 0 coins? I feel bad, here take 10 coins!")
		sleep(2)
		addCoins(value: 10)
		sleep(1)
	}
}
//
//
func openInventory() {
	print(success + "Inventory:")
	if Matches != 0 {
		print(String(Matches) + " x Matches")
	}
	if Sticks != 0 {
		print(String(Sticks) + " x Sticks")
	}
	if basicHealingPotion != 0 {
		print(String(basicHealingPotion) + " x Basic Healing Potion")
	}
	if Sword != 0 {
		// TODO: Implement more then just a basic sword.
		print("Basic Sword")
	}
	// This print just adds some white space

	print(" " + WHITE)
}

func randomEvent() {
    print("This is a randomly generated event! The stories in here have not been completed yet.\n")

    let randomLoop = true

	if events.count > 0 {
		let selection = events.randomElement()!
		if selection == "store" {
            print("Store selected\n")
		} else if selection == "randomFight" {
            print("randomFight selected\n")
		}
		events.removeFirst()
	} else {
        print("There are no more unvisited events left!\n")
	}
}

func useMatch() {
	if Matches == 0 {
		print(error + "You don't have any matches!\n" + WHITE)

	} else if surroundingsLit == true {
		Matches = Matches - 1
		CSDescription = "This place is in ruins, possibly for decades."
		print("You light a match. it begins to burn away.")
		print(rip + "You used up one match. \n" + WHITE)
	} else if surroundingsLit == false {

		CSDescription = "This place is in ruins, possibly for decades."
		Matches = Matches - 1
		surroundingsLit = true
		print("You Light a match, your surroundings fill up with light.",
		"You can now see!")
		print(rip + "You used up one match. \n")

	}
}


func start() {
	if surroundingsLit == false {
        print("You find yourself in an odd and dark place... \nWhat could this possibly be?\n")
        CSDescription = "This place is extremely dark, you can't see anything..."
        sleep(2)

        print("Check your inventory, you might have something to \nimprove your vision...\n")
        sleep(2)
        // combat("Bob", 69)
        //print("Maybe I should use a match to light this place up...") // too straight forward.

        //print(hint + "type 'm' to use a match)\n" + Style.RESET_ALL) // too straight forward.
	} else {
		if currentScene == 1 {
            print("This place looks like it's been abandoned decades ago...") // NOTE: describe this 'place'!
            print(action + "An odd creature begins to walk up to you... \n") // NOTE: describe this 'creature'! e.g. this oddly hunched over creature
			let answer = ask(funcQuestion: "Should you hide or comfront them?", answer1: "h", answer2: "c")
			if answer == "c" {
                // User selected comfront
                // Nothing special happens, it is passed on to the next part
			} else if answer == "h" {
                // User selected hide
                print(action + "You tried to hide, but there was nowhere to go, the figure began to confront you.")
                sleep(3)
			}
            print(action + "The odd figure got close enough until you could see it.") // NOTE: so is this a creature or figure?
            sleep(2)

            print(action + "The figure looked like an ancient wizard. \n")
            sleep(2) //

			print(quote + "Greetings, it seems you are new here,  is that true?" + WHITE, terminator:"")
			_ = readLine()

            // NOTE: maybe. give the user a choice to say something.
            print(action + "You said yes. \n")
            sleep(1)

            print(quote + "I see, this is a dangerous place, so tread carefully..." + WHITE) // ITS DANGEROUS TO GO ALONE.
            sleep(2)

            print(quote + "Here, take this, it will help you defend yourself." + WHITE)
            sleep(3) // TAKE THIS.

            print(success + "You recieved a basic sword.")
            print(success + "You recieved a basic healing potion.")
			addCoins(value: 50)


            basicHealingPotion = basicHealingPotion + 1
            Sword = 1
            currentScene = 2

		} else if currentScene == 2 {
            print(action + "You ask the ancient wizard:")
            sleep(1)

            print(WHITE + "Who are you?")
            sleep(1)
            print("What is this place? \n")
            sleep(1)

            print(action + "The wizard responds \n")
            sleep(1)

            print(quote + """
This place is an underground town, it used to be
thriving, there were plenty of stores, lots of jobs, it was
a great place to be...\n But then, the rebellion came in
and wiped this place out, everybody either escaped or died.
And me, I was the founder of this town.
"""  + WHITE)
            sleep(8)
            CSDescription = "This place is in ruins, apparently it's supposed to be a town...\nThere is a door to the next room, something seems to be strung across it."

			print(quote + "Would you like to recieve a quest?" + WHITE, terminator:"")
			_ = readLine()
            print(action + "You said yes. \n")
            sleep(1)

            print(quote + """
			Try and recover the Great Stone of Knowledge,
			it is located in the north-east room, however it is guarded
			by very powerful Almogates.
			""" + WHITE)
            sleep(5)

            print(quote + "Good luck." + WHITE)
            sleep(2)

            print(action + "He leaves the room and now, you're on your own. \n")
            currentScene = 3

		} else if currentScene == 3 {
            CSDescription = "The room looked very charred after the explosion."

            print(action + "After the wizard left, you went into the next room. \n")
            sleep(2)

            print(action + "It is odly quiet here... you begin to look around... \n")
            sleep(3)

            print(rip + "BANG! A small bomb exploded, it was a trap!")
			damage(value: 20)
            sleep(2)
            currentScene = 4

		} else if currentScene == 4 {
            print(action + "You proceed to the next room, being very careful where you step.")

            CSDescription = "This room is rather empty, but an old and dried up fountain lays ahead.\na few coins lay scattered across the bottom, maybe you can pick them up..."
            coinsInScene = true
            sleep(2)

            print(action + "You quickly hear a movement and freeze...\n")
			sleep(2)

            print(quote + "IT WAS YOU WHO DID IT! Y-YOU WERE THE ONE WHO KILLED ALL M -MY F-F-FRIENDS!"  + WHITE)
            sleep(3)
            print(action + "You try to explain that they were mistaken but it was too late. \n")
            sleep(2)


			let theResult = combat(enemy: "Unidentified", enemyHP: 25)
			if theResult == "kill" {
                print(action + "You killed the unknown person however, you can't stop feeling bad. \n")
			} else if theResult == "flee" {
                print(action + "You quickly ran away, you're safe now. \n")
			}
            currentScene = 5

		} else if currentScene == 5{
            // It is done bois!
            randomEvent()
		}
	}
}


func hpCheck() {
    // Displays different colour depending on hp

	if hp > 70 {
        print(success + "You have " + String(hp) + " out of 100 HP!")
	}
	else if hp > 35 {
        print(action + "You have " + String(hp) + " out of 100 HP!")

	} else {
        print(rip + "You have " + String(hp) + " out of 100 HP!")
	}
}



func lookAround() {
    print(CSDescription)
}

func pickCoins(){

	if coinsInScene == true {
        let amount = Int.random(in: 4..<6)
        print(action + "You reach down and pick up all the coins from the floor.")
        sleep(1)

		addCoins(value: amount)
        coinsInScene = false


	} else {
        print(error + "There are no coins to pick up! \n")
	}
}


func main() {
	print(CYAN + "[Action] " + WHITE, terminator:"")
    let command = readLine()

	let chkMoney = ["check money", "check coins", "coins", "money", "c"]
	let opnInvnt = ["open inventory", "open inv" ,"inventory", "inv", "i","check inventory", "check inv"]
	let cmdMatch = ["use match", "strike match", "match", "light match",
	"use matches", "matches", "m"]
	let helpMenu = ["h", "help", "umm", "asdfghjkl", "qwertyuiop"]
	let exitComd = ["e", "exit", "close", "alt-f4"]
	let showHlth = ["hp", "health", "health points"]
	let startCmd = ["s", "start", "next", "proceed", "next room", "forth"]
	let lookArnd = ["l", "look around", "look", "observe"]

	if chkMoney.contains(command!) {
        checkCoins()
	} else if opnInvnt.contains(command!) {
        openInventory()
	} else if cmdMatch.contains(command!) {
        useMatch()
	} else if helpMenu.contains(command!) {
		print("help")
	} else if exitComd.contains(command!) {
        mainLoop = 0
	} else if showHlth.contains(command!) {
        hpCheck()
	} else if startCmd.contains(command!) {
        start()
	} else if lookArnd.contains(command!) {
        lookAround()
	}

	let Pickupcoins = ["pickup coins", "pick up coins", "pick coins"]

	if Pickupcoins.contains(command!) {
        pickCoins()
	}
}

//// Introduce the user:
print("Welcome to " + GREEN + "DungeonCli!" + WHITE)
print(BOLD + "Type 'h' for help or 's' to start! \n")
//
//// Run those functions here:
repeat {
    main()
} while mainLoop == 1
