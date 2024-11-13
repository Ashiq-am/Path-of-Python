# importing libraries.
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# storing image path
fname = r'geeks.png'

# opening image using pil
image = Image.open(fname).convert("L")

# maping image to gray scale
plt.imshow(image, cmap='gray')
plt.show()
