# importing editor from movie py
from moviepy.editor import *

# importing numpy
import numpy as np

# method to create a fram
def make_frame(t):
	numpy_array = np.array([1, 2, 4, 1, 3, 4, 5])
	return numpy_array


# creating audio clip
clip = AudioClip(make_frame, duration = 3)

# printing audio clip
print(clip)
