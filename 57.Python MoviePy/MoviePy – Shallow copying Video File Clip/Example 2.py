# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# shallow copy the given clip
copied_clip = clip.copy()

# showing clip
copied_clip.ipython_display(width = 360)
