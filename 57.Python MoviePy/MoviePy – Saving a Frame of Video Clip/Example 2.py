# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")


# getting duration of the video
duration = clip.duration

# saving a frame at 1 second
clip.save_frame("frame1.png", t = 1)

# showing clip
clip.ipython_display(width = 360)
