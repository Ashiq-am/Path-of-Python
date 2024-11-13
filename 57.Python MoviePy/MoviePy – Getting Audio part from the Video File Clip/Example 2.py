# Import everything needed to edit video clips
from moviepy.editor import *


# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")


# getting only first 3 seconds
clip = clip.subclip(0, 3)

# getting audio from the clip
audioclip = clip.audio

# printing audio clip
print(audioclip)
