# importing editor from movie py
from moviepy.editor import *


# creating a color clip
# setting it size to be 200 x 200
clip = ColorClip(size =(200, 200), color =[255, 255, 100])

# showing clip
clip.ipython_display()
