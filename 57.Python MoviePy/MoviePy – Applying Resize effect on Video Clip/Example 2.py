# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting subclip from it
clip = clip.subclip(0, 5)

# applying resize filter
final = clip.fx( vfx.resize, width = 280)

# showing final clip
final.ipython_display()
