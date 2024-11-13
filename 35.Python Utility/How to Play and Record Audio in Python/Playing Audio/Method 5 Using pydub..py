from pydub import AudioSegment
from pydub.playback import play

tape = AudioSegment.from_file('path_to_myfile.wav', format='wav')
tape = AudioSegment.from_wav('path_to_myfile.wav')

play(tape)
