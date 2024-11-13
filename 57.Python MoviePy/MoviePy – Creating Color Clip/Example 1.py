# importing editor from movie py
from moviepy.editor import *


# creating a color clip
# setting it size to be 460 x 380
clip = ColorClip(size =(460, 380), color =[100, 255, 100])

# showing clip
clip.ipython_display()
