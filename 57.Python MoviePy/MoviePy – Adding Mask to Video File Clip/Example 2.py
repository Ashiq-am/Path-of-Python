# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# add mask to the clip
clip = clip.add_mask()


# displaying new clip
clip.ipython_display(width = 420)
