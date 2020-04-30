##### using simpleaudio directly:
import simpleaudio
import pydub
import time

sound = (pydub.AudioSegment.from_ogg("sounds/explosion.ogg") * 20)

playback = simpleaudio.play_buffer(
    sound.raw_data,
    num_channels=sound.channels,
    bytes_per_sample=sound.sample_width,
    sample_rate=sound.frame_rate
)

# end playback after 3 seconds
time.sleep(3)
playback.stop()
