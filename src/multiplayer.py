# oh boi here we go
import sys
import threading
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
	}
]
answers = prompt(questions)
serverIP = answers['serverIP']
yourUserName = answers['username']


r = RethinkDB()
connection = r.connect(serverIP, 28015)
def checkMessages():
	connection.repl()
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
		'message': 'Enter message',
		'name': 'yourMessage',
	},
]
answers = prompt(questions)
yourMessage = answers['yourMessage']
connection.repl()
r.table('chat').insert({'username':yourUserName, 'message':yourMessage}).run()
