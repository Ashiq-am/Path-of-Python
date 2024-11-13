# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# creating numpy linspace
z1 = np.linspace(0, np.pi)

# creating numpy meshgrid
X, Y = np.meshgrid(z1, z1)

# creating rgb channels
# creating red channel through sin function
red = np.sin(X)

# creating green channel through cos function
green = np.cos(4 * Y)

# creating blue channel
blue = X * Y

# creating rgb image from these three channel
img = mahotas.as_rgb(red, green, blue)

# showing image
imshow(img)
show()
