import time

from pydub import generators
from pydub.playback import _play_with_simpleaudio
import pydub

# 5 seconds of A 440


##### using pydub's helper function:
playback = _play_with_simpleaudio(pydub.AudioSegment.from_mp3("Music/spaceCruise.mp3"))

# end playback after 3 seconds
time.sleep(3)
playback.stop()
