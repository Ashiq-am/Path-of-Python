# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip from it
clip1 = clip.subclip(0, 10)

# getting width of the clip
width = clip1.w

# printing value of width
print("Width of clip : " + str(width))


print("---------------------------------------")


# showing final clip
clip1.ipython_display(width = 480)
