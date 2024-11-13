# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# showing clip
clip.ipython_display(width = 360)

# releasing the video file clip
clip.close()
