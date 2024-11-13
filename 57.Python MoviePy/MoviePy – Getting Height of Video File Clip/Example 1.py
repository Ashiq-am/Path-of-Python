# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip from it
clip1 = clip.subclip(0, 10)

# getting height of the clip
height = clip1.h

# printing value of width
print("Height of clip : " + str(height))


print("---------------------------------------")


# showing final clip
clip1.ipython_display(width = 480)
