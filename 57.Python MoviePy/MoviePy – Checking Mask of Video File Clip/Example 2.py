# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# masking this clip as amsk
clip = clip.set_ismask(True)

# checking if clip is mask
value = clip.ismask

# printing value
print("Clip is Mask ", end = " : ")
print(value)

# displaying new clip
clip.ipython_display()
