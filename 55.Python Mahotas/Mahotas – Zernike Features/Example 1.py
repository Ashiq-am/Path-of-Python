# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np
import matplotlib.pyplot as plt

# loading image
img = mahotas.demos.load('lena')

# filtering image
img = img.max(2)

print("Image")

# showing image
imshow(img)
show()

# degree
degree = 10

# radius
radius = 10

# computing zernike feature
value = mahotas.features.zernike(img, degree, radius)


# printing value
print(value)
