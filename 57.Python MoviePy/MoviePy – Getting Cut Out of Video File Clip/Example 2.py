# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting only first 5 seconds
clip = clip.subclip(0, 10)

# cutting out some part from the clip
clip = clip.cutout(3, 7)

# showing clip
clip.ipython_display(width=360)
