# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting subclip
clip = clip.subclip(0, 7)

# rotating clip by 180 degree
clip = clip.rotate(180)

# showing clip
clip.ipython_display()
