# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# creating array of shape 50x50
# for red channel
r = np.arange(2500).reshape(50, 50)

# for blue channel
g = np.arange(2500).reshape(50, 50)

# for blue channel
b = np.arange(2500).reshape(50, 50)

# making red channel values to 0
r = r * 0

# increasing green channel values
g = g * 100

# making blue channel values to 0
b = b * 0

# creating rgb image from these three channel
img = mahotas.as_rgb(r, g, b)

# showing image
imshow(img)
show()
