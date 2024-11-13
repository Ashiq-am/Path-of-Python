# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 2 seconds
clip = clip.subclip(0, 2)

# new clip with new end time
new_clip = clip.set_end(3)

# displaying new clip
new_clip.ipython_display(width = 360)
