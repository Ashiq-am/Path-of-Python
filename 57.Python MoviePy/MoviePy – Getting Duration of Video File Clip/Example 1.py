# Import everything needed to edit video clips
from moviepy.editor import *


# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting duration of the video
duration = clip.duration

# printing duration
print("Duration : " + str(duration))

# showing final clip
clip.ipython_display()
