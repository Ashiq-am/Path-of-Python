# importing editor from movie py
from moviepy.editor import *

# importing numpy
import numpy as np

# method to create a fram
def make_frame(t):
	numpy_array = np.array([1, 2, 3, 1])*t
	return numpy_array


# creating audio clip
clip = AudioClip(make_frame, duration = 3)

# printing audio clip
print(clip)
