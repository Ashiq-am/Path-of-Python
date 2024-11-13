# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting subclip
clip = clip.subclip(0, 7)

# saving the clip
clip.write_videofile("handmade_gfg.mp4")

# showing clip
clip.ipython_display()
