# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip1 = clip.subclip(0, 7)

# mirroring image according to the y axis
clip = clip.fx(vfx.mirror_y)


# showing final clip
clip.ipython_display()
