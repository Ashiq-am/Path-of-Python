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

# computing Parameters of the ‘image ellipse’
semimajor, semiminor = mahotas.features.ellipse_axes(img)


# showing value
print("Semi Major Exes : " + str(semimajor))
print("Semi Minor Exes : " + str(semiminor))
