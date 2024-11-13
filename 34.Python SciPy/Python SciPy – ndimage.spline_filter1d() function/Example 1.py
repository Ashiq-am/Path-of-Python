# importing spline filter with one dimension.
from scipy.ndimage import spline_filter1d

# importing matplot library for visualiation
import matplotlib.pyplot as plt

# importing munpy module
import numpy as np

# creating an image
geek_image = np.eye(80)

# returns an image array format
geek_image[40, :] = 1.0
print(geek_image)
