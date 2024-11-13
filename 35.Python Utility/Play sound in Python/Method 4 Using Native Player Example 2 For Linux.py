# import required module
import os

# play sound
file = "note.mp3"
print('playing sound using native player')
os.system("mpg123 " + file)
