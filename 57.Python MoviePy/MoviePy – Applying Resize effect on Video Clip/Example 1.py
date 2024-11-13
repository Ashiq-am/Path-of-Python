# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# applying resize filter
final = clip.fx( vfx.resize, width = 280)

# showing final clip
final.ipython_display()
