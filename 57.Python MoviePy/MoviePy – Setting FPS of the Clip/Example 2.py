# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# new clip with new fps
new_clip = clip.set_fps(100)

# displaying new clip
new_clip.ipython_display(width = 360)
