# python code to load and visualize
# an image

# import necessary libraries
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# load the image
img_path = 'Koala.jpg'
img = Image.open(img_path)

# convert PIL image to numpy array
img_np = np.array(img)

# plot the pixel values
plt.hist(img_np.ravel(), bins=50, density=True)
plt.xlabel("pixel values")
plt.ylabel("relative frequency")
plt.title("distribution of pixels")
