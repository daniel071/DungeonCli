# oh boi here we go
import sys
sys.path.append('../')

from colorama import Fore, Back, Style
from colorama import init
from PyInquirer import prompt, print_json
# <<< import DungeonCli >>>
# idk why this import takes ageeessss
# maybe because its 2000 lines hmmm...

from rethinkdb import RethinkDB

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
		'default': ''
	}
]
answers = prompt(questions)
serverIP = answers['serverIP']
yourUserName = answers['username']


r = RethinkDB()
r.connect(serverIP, 28015).repl()

cursor = r.table("chat").changes().run()
for document in cursor:
	username = document['new_val']['username']
	message = document['new_val']['message']

	print(Style.BRIGHT + Fore.YELLOW + "[{username}]: ".format(username=username)
	+ Style.RESET_ALL + "{message}".format(message=message))
	print(document)
