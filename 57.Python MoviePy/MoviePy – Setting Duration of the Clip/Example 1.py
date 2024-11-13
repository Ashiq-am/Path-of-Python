# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# new clip with new duration
new_clip = clip.set_duration(10)

# new clip with new duration
new_clip.ipython_display(width=360)
