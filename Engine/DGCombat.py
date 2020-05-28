# The combat system. Use DGCombat.combat()

from . import DGText
from . import DGScene
from . import DGMain
from . import DGPlayer
from colorama import Fore, Back, Style
from colorama import init
from PyInquirer import prompt, print_json
import time
import random

battleSongs = ["Music/Ambient_fight_1.ogg", "Music/interstellar_space_dryer_2.ogg"]
Scene = DGScene

def combat(enemy, enemyHP, enemyMinDamage, enemyMaxDamage):
	global DGPlayer
	global combatEnemyHP
	global hasCombatFinished

	hasCombatFinished = "no."


	def finishUpMusic():
		DGMain.endThreads()
		DGMain.playSound("Music/quest.ogg", True)



	def enemyDealDamage(multiplyer):
		global DGPlayer
		isMiss = random.randint(1,6)
		if isMiss == 5:
			DGText.printScan(action + "{name} missed!".format(name=enemy))
			DGText.printScan(DGText.success + "You took no damage!\n")
		else:
			enemyDamage = random.randint(enemyMinDamage, enemyMaxDamage) * DGPlayer.Inventory.absorbtion * multiplyer
			DGPlayer.hp = DGPlayer.hp - enemyDamage

			DGText.printScan(DGText.rip + "{name} deals {damage} damage!"
			.format(damage=round(enemyDamage), name=enemy))
			time.sleep(0.4)
			if DGPlayer.hp < 0:
				combatLoop == False

			DGMain.isDead()


	def playerDealDamage(enemyHP):
		# for some reason this function couldn't use enemyhp???? so I made
		# a seperate one so it would work... :)

		global hasCombatFinished
		global combatLoop
		global DGPlayer

		isMiss = random.randint(1,7)
		isCritical = random.randint(1, 5)
		if isMiss == 1:
			DGText.printScan(DGText.action + "You missed!")
			DGText.printScan(DGText.rip + "You dealt no damage!")


		else:
			playerDamage = random.randint(5, 10)
			playerDamage = playerDamage * DGPlayer.Inventory.damage
			enemyHP = enemyHP - playerDamage

			if isCritical == 1:
				DGText.printScan(DGText.success + "Critical hit!")
				DGText.printScan(DGText.success + "You deal double damage!\n")
				playerDamage = playerDamage * 2

			DGText.printScan(DGText.success + "You deal {damage} damage!".format(damage=round(playerDamage)))
			time.sleep(0.2)

			if enemyHP < 0:
				combatLoop = False
				DGText.printScan(DGText.success + "You DGText.successfully killed {name}\n"
				.format(name=enemy))

				time.sleep(0.4)

				extraCoins = random.randint(25, 35)
				addCoins(extraCoins)

				combatLoop = False

				finishUpMusic()

				hasCombatFinished = "killed"

		if Scene.combatOverrideMusic == False:
			regenerated = random.randint(1000, 2000)
			enemyHP = enemyHP + regenerated
			DGText.printScan(DGText.rip + "The boss regenerated {amount} hp!".format(amount=regenerated))

		return enemyHP


	if Scene.combatOverrideMusic == True:
		DGMain.endThreads()
		songToPlay = random.choice(battleSongs)
		DGMain.playSound(songToPlay, True)

	global DGPlayer
	DGText.printScan(DGText.rip + "You get in a battle with {enemy}!\n".format(enemy=enemy) + Style.RESET_ALL)
	time.sleep(0.5)

	questions = [
		{
			'type': 'list',
			'name': 'userChoice',
					'choices': ['Fight',
								'Flee',
								'Use item',
								'Check HP'],
			'message': 'What would you like to do?',
		}
	]

	combatLoop = True
	while combatLoop:
		if hasCombatFinished == "killed":
			combatLoop = False
			return "killed"


		print(Style.RESET_ALL)
		answers = prompt(questions)
		userInput = answers['userChoice']
		if userInput == "Fight":
			enemyDealDamage(1)
			enemyHP = playerDealDamage(enemyHP)


		elif userInput == "Flee":
			attemptFlee = random.randint(1, 2)
			if attemptFlee == 1:
				DGText.printScan(action + "You tried to flee, but {name} caught you. \n"
				.format(name=enemy))
				enemyDealDamage(1.5)

			else:
				DGText.printScan(action + "You run away before {name} could catch you.\n"
				.format(name=enemy))
				combatLoop = False
				time.sleep(0.4)

				finishUpMusic()

				return "flee"

		elif userInput == "Use item":
			potionQuestion = [
				{
					'type': 'list',
					'name': 'userChoice',
							'choices': ['Healing Potion',
										'Poison Potion',],
					'message': 'What potion type would you like to use?',
				}
			]

			theAnswer = prompt(potionQuestion)
			theEpicOption = theAnswer['userChoice']

			if theEpicOption == "Healing Potion":
				theOutput = healingPotion()
				if theOutput != "notUsed":
					if theOutput != 0:
						i = 0
						while i < theOutput:
							enemyDealDamage(1)
							i = i + 1


			elif theEpicOption == "Poison Potion":
				theOutput = usePoisonPotion()
				if theOutput != 0:
					# Saves current damage, multiplies it by 3 then sets it back.
					originalDamage = DGPlayer.Inventory.damage
					DGPlayer.Inventory.damage = DGPlayer.Inventory.damage * 3
					playerDealDamage(enemyHP)
					DGPlayer.Inventory.damage = originalDamage


		elif userInput == "Check HP":
			hpCheck()
			DGText.printScan(action + "The enemy has {amount} hp!\n".format(amount=round(enemyHP)))
			time.sleep(0.2)

		print("")
