# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip from the original video
clip = clip.subclip(0, 10)

# adding margin to the video
clip = clip.margin(40)


# showing final clip
clip.ipython_display()
