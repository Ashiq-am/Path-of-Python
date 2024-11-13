# importing editor from movie py
from moviepy.editor import *

# creating a Image sequence clip with fps = 1
clip = ImageSequenceClip(['frame1.png', 'frame2.png', 'frame1.png', 'frame2.png'], fps = 1)

# showing clip
clip.ipython_display(width = 360)
