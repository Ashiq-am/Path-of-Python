# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting start time of the clip
value = clip.start

# printing start time
print("Start Time : ", end=" ")
print(value)

# showing clip
clip.ipython_display(width=360)
