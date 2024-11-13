# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip from the original video
clip = clip.subclip(0, 10)

# mirroring image according to the y axis
clip = clip.fx(vfx.mirror_y)


# showing final clip
clip.ipython_display()
