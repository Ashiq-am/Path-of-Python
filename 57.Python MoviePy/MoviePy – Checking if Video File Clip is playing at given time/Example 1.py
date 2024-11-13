# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# checking if clip will be playing at time 2
value = clip.is_playing(2)

# printing the value
print("Clip will be playing at time = 2 ", end=" : ")
print(value)

# showing clip
clip.ipython_display(width=360)
