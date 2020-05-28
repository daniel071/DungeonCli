import time
from colorama import Fore, Back, Style
from colorama import init

success = Style.BRIGHT + Fore.GREEN + "==> "
rip = Style.BRIGHT + Fore.RED + "==> "
question = Style.BRIGHT + Fore.YELLOW + "[?] "
error = Style.BRIGHT + Fore.RED + "[!] "
hint = Style.DIM + Fore.WHITE + "(hint: "
action = Style.BRIGHT + Fore.YELLOW + "==> "
quote = Style.BRIGHT + Fore.WHITE + '"'
info = Style.BRIGHT + Fore.WHITE + "==> " + Style.RESET_ALL
askPrompt = Style.BRIGHT + Fore.CYAN

def printScan(toPrint):
	printspeed = 0.013

	for letter in toPrint:
		print(letter, end='', flush=True)
		time.sleep(printspeed)


	print("\r", flush=True)
