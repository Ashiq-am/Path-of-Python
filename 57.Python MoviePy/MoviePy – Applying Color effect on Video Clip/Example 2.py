# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip = clip.subclip(0, 9)


# applying color effect
final = clip.fx( vfx.colorx, 0.5)

# showing final clip
final.ipython_display()
