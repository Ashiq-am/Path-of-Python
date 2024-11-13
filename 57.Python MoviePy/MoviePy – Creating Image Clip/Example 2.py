# importing editor from movie py
from moviepy.editor import *

# file name
name = "frame2.png"

# creating a image clip
clip = ImageClip(name)

# showing clip
clip.ipython_display()
