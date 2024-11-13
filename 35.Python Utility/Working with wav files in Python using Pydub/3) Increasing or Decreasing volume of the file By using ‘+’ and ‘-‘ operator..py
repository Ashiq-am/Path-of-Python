# import required library
import pydub
from pydub.playback import play

wav_file = pydub.AudioSegment.from_file(file = "Sample.wav",
										format = "wav")
# Increase the volume by 10 dB
new_wav_file = wav_file + 10

# Reducing volume by 5
silent_wav_file = wav_file - 5

# Playing silent file
play(silent_wav_file)

# Playing original file
play(wav_file)

# Playing louder file
play(new_wav_file)

# Feel the difference!
