import time

from pydub import generators
from pydub.playback import _play_with_simpleaudio
import pydub

# 5 seconds of A 440
printspeed = 0.013
defprntspd = 0.013

def printScan(toPrint):
	global printspeed
	printspeed = defprntspd

	for letter in toPrint:
		print(letter, end='', flush=True)
		time.sleep(printspeed)


	print("\r", flush=True)

##### using pydub's helper function:
playback = _play_with_simpleaudio(pydub.AudioSegment.from_mp3("Music/spaceCruise.mp3") )

# end playback after 3 seconds
time.sleep(3)
playback.stop()

playback3 = _play_with_simpleaudio(pydub.AudioSegment.from_mp3("Sounds/explosion.wav") * 32)
##### using simpleaudio directly

printScan("Sample Text! Hello World! im a poppen gamer? idk what im typing")
playback.stop()
