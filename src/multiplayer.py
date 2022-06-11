# oh boi here we go
import sys
import multiprocessing
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
sys.path.insert(0, './Game/Engine')
import DGText
import rethinkdb as rdb

# advertising ;)
default = 'pavela.net'
defaultUsername = ''

def runMe():
	global default
	global defaultUsername
	questions = [
		{
			'type': 'input',
			'message': 'Enter server IP',
			'name': 'serverIP',
			'default': default
		},
		{
			'type': 'input',
			'message': 'Enter your username',
			'name': 'username',
			'default': defaultUsername
		}
	]
	answers = prompt(questions)
	serverIP = answers['serverIP']
	yourUserName = answers['username']
	default = serverIP
	defaultUsername = yourUserName

	try:
		r = rdb.RethinkDB()
		r.connect(serverIP, 28015).repl()
	except r.errors.ReqlDriverError:
		print(DGText.error + "Server connection failed!\n")
		return


	def checkMessages():
		r2 = rdb.RethinkDB()
		r2.connect(serverIP, 28015).repl()
		cursor = r2.table("chat").changes().run()
		for document in cursor:
			username = document['new_val']['username']
			message = document['new_val']['message']

			print(Style.BRIGHT + Fore.YELLOW + "[{username}]: ".format(username=username)
			+ Style.RESET_ALL + "{message}".format(message=message))

	def checkPlayerChanges():
		r3 = rdb.RethinkDB()
		r3.connect(serverIP, 28015).repl()
		cursor = r3.table("clients").changes().run()
		for document in cursor:
			print()
			new_val = document['new_val']
			old_val = document['old_val']

			if new_val:
				print(DGText.playerEvent + " {client} has joined the lobby!".format(client=new_val['client']))
			if old_val:
				print(DGText.playerEvent + " {client} has left the lobby!".format(client=old_val['client']))

	checkThread = multiprocessing.Process(target=checkMessages, args=())
	checkThread.start()

	checkPlayersThread = multiprocessing.Process(target=checkPlayerChanges, args=())
	checkPlayersThread.start()

	questions = [
		{
			'type': 'input',
			'message': '>',
			'name': 'yourMessage',
		},
	]

	r.table('clients').insert([{"client":yourUserName}]).run()

	print(DGText.loading + "Welcome to the lobby!")
	print(DGText.loading + "Run /help for instructions and /start to begin.")

	while True:
		answers = prompt(questions)
		yourMessage = answers['yourMessage']

		if yourMessage.lower() == "/exit":
			print()
			checkThread.terminate()
			checkPlayersThread.terminate()
			r.table("clients").filter({"client": yourUserName}).delete().run()
			raise EOFError()

		elif yourMessage.lower() == "/help":
			print("Commands: /exit, /help, /players, /start")
		elif yourMessage.lower() == "/players" or yourMessage.lower() == "/list":
			print(r.table("clients").run())
		elif yourMessage.lower() == "/start":
			# add starting functions here
			pass
		else:
			#sys.stdout.write("\033[F") # Clears the text above
			r.table('chat').insert([{"username":yourUserName, "message":yourMessage}]).run()
