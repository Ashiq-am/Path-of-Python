# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting subclip as video is large
clip = clip.subclip(55, 65)

# saving the clip
clip.write_videofile("gfg_intro.webm")

# showing clip
clip.ipython_display(width = 480)
