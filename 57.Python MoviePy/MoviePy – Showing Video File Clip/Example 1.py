# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip as video is large
clip = clip.subclip(0, 10)


# showing clip
clip.ipython_display(width = 280, height = 320)
