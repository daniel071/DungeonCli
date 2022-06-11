# oh boi here we go
import sys
import threading
sys.path.append('../')

# Fix python 3.10 support for rethinkdb
import collections
collections.Callable = collections.abc.Callable
collections.Mapping = collections.abc.Mapping
collections.Iterable = collections.abc.Iterable

import json
from colorama import Fore, Back, Style
from colorama import init
from PyInquirer import prompt, print_json
# <<< import DungeonCli >>>
# idk why this import takes ageeessss
# maybe because its 2000 lines hmmm...

import rethinkdb as rdb

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


	r = rdb.RethinkDB()

	def checkMessages():
		r.connect(serverIP, 28015).repl()
		cursor = r.table("chat").changes().run()
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
		r.connect(serverIP, 28015).repl()
		r.table('chat').insert([{"username":yourUserName, "message":yourMessage}]).run()
