# importing various libraries
import numpy as np
import mahotas
import mahotas.demos
from mahotas.thresholding import soft_threshold
from pylab import imshow, show
from os import path

# loading image
f = mahotas.demos.load('luispedro', as_grey = True)


# showing image
print("Image")

imshow(f)
show()

# haar transform
h = mahotas.haar(f)

# showing image
print("Image with haar transform")
imshow(h)
show()
