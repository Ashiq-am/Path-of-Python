# import required module
import os

# play sound
file = "note.wav"
print('playing sound using native player')
os.system("afplay " + file)
