# importing matplotlib
from matplotlib import pyplot as plt

# importing numpy
import numpy as np

# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
clip = VideoFileClip("geeks.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting frame at time 3
frame = clip.get_frame(3)

# showing the frame with the help of matplotlib
plt.imshow(frame, interpolation='nearest')

# show
plt.show()
