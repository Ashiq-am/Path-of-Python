# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip as video is large
clip = clip.subclip(55, 65)

# rotating clip by 45 degree
clip = clip.rotate(45)

# showing clip
clip.ipython_display(width = 480)
