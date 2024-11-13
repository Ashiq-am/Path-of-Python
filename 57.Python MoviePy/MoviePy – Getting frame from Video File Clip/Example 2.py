# importing matplotlib
from matplotlib import pyplot as plt

# importing numpy
import numpy as np

# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting frame at time 2
frame = clip.get_frame(2)

# showing the frame with the help of matplotlib
plt.imshow(frame, interpolation='nearest')

# show
plt.show()
