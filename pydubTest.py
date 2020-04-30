import time

from pydub import generators
from pydub.playback import _play_with_simpleaudio

# 5 seconds of A 440
sound = generators.Sine(440).to_audio_segment(duration=5000)

##### using pydub's helper function:
playback = _play_with_simpleaudio(audio_segment)

# end playback after 3 seconds
time.sleep(3)
playback.stop()

##### using simpleaudio directly:
import simpleaudio
playback = simpleaudio.play_buffer(
    sound.raw_data,
    num_channels=sound.channels,
    bytes_per_sample=sound.sample_width,
    sample_rate=sound.frame_rate
)
# end playback after 3 seconds
time.sleep(3)
playback.stop()
