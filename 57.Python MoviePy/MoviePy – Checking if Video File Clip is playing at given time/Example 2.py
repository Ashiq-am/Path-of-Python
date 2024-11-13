# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# checking if clip will be playing at time 8
value = clip.is_playing(8)

# printing the value
print("Clip will be playing at time = 8 ", end=" : ")
print(value)

# showing clip
clip.ipython_display(width=360)
