##### using simpleaudio directly:
import simpleaudio
import pydub
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sound = (pydub.AudioSegment.from_ogg("Sounds/explosion.ogg") * 20)
playback = simpleaudio.play_buffer(
    sound.raw_data,
    num_channels=sound.channels,
    bytes_per_sample=sound.sample_width,
    sample_rate=sound.frame_rate
)
time.sleep(3)
playback.stop()
