# oh boi here we go
import sys
import threading
sys.path.append('../')

import json
from colorama import Fore, Back, Style
from colorama import init
from PyInquirer import prompt, print_json
# <<< import DungeonCli >>>
# idk why this import takes ageeessss
# maybe because its 2000 lines hmmm...

from rethinkdb import RethinkDB

def runMe():
	questions = [
		{
			'type': 'input',
			'message': 'Enter server IP',
			'name': 'serverIP',
			'default': 'pavela.net'
		},
		{
			'type': 'input',
			'message': 'Enter your username',
			'name': 'username',
		}
	]
	answers = prompt(questions)
	serverIP = answers['serverIP']
	yourUserName = answers['username']


	r1 = RethinkDB()
	r2 = RethinkDB()

	def checkMessages():
		r1.connect(serverIP, 28015).repl()
		cursor = r1.table("chat").changes().run()
		for document in cursor:
			username = document['new_val']['username']
			message = document['new_val']['message']

			print(Style.BRIGHT + Fore.YELLOW + "[{username}]: ".format(username=username)
			+ Style.RESET_ALL + "{message}".format(message=message))


	checkThread = threading.Thread(target=checkMessages)
	checkThread.start()
	# To stop thread: checkThread.join()

	questions = [
		{
			'type': 'input',
			'message': '>',
			'name': 'yourMessage',
		},
	]
	while True:
		answers = prompt(questions)
		yourMessage = answers['yourMessage']
		sys.stdout.write("\033[F") # Clears the text above
		r2.connect(serverIP, 28015).repl()
		r2.table('chat').insert([{"username":yourUserName, "message":yourMessage}]).run()
