# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# checking if clip is mask
value = clip.ismask

# printing value
print("Clip is Mask ", end=" : ")
print(value)

# displaying new clip
clip.ipython_display(width=420)
