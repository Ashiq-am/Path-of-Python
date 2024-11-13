# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip1 = clip.subclip(0, 7)

# getting height of the clip
height = clip1.h

# printing value of width
print("Height of clip : " + str(height))



print("---------------------------------------")


# showing final clip
clip1.ipython_display()
