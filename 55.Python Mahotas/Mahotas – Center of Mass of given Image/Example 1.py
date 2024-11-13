# importing required libraries
# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
img = mahotas.demos.load('lena')

# grey image
g = img[:, :, 1]

# multiplying grey image values
g = g * 100

# filtering image
img = img.max(2)

# showing image
imshow(img)
show()

# getting center of mass
center = mahotas.center_of_mass(img)

# printing center of mass co-ordinate
print("Center of Mass : " + str(center))
