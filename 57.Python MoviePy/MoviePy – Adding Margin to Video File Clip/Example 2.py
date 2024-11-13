# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip1 = clip.subclip(0, 7)

# adding margin to the clip
clip1 = clip1.margin(20)


# showing final clip
clip1.ipython_display()
