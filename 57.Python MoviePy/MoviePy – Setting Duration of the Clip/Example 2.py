# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 2 seconds
clip = clip.subclip(0, 2)

# new clip with new duration
new_clip = clip.set_duration(6)

# showing clip
new_clip.ipython_display(width = 360)
