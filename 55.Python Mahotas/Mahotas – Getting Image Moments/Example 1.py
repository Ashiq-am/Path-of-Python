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

# Power for first dimension
p0 = 5.5

# Power for second dimension
p1 = 5.5


# getting moments
moment = mahotas.moments(img, p0, p1)


# printing moments
print("Moment value = " + str(moment))
