# The random dialog class. It contains multiple lists of possible dialogs for
# an event.

import random

class randomDialog:
	def bombExplodes(self):
		dialog=["A small bomb exploded, it was a trap!\n",
		"Ouch! You tripped a small Bomb trap!\n",
		"You attempted to avoid the obvious trap, however it set off a small bomb!\n"]

		return random.choice(dialog)


	def collectCoins(self):
		dialog=["You reach out and grab all the coins.",
		"You stuff your pockets with the coins.",
		"You reach out in awe to consieve all the coins."]
		return random.choice(dialog)


	def gameoverText(self):
		dialog=["Maybe next time, you might be a bit more lucky...\n",
		"Maybe next time, things might be in your favour...\n",
		"Maybe next time, you'll be more careful...\n",
		"Maybe next time, you might not be where you are now...\n",
		"Maybe next time, you'll be more wise...\n",
		"Maybe next time, you'll choose the right option...\n",
		"Maybe next time, you won't be so careless...\n",
		"Maybe next time, things might actually go right...\n",
		"Maybe next time, you'll remember that you are mortal...\n"]
		return random.choice(dialog)

	def roomDescription(self):
		dialog=["The ceiling in this room hangs really low. Seeing it is truly a strange sight.",
		"It's oddly ambient in here, water trickles down the walls. It's rather relaxing.",
		"This room is massive."]
		return random.choice(dialog)

	def coinsOnFloor(self):
		dialog=["There are some coins on the floor.",
		"Some coins are scattered on the ground.",
		"There are some coins nearby."]
		return random.choice(dialog)
	def store(self):
		dialog=["There is a store in this room.",
		"And old store is setup in here..",
		"An old shack with the letters \'Store\' is nearby."]
		return random.choice(dialog)
