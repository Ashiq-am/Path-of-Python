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

# making image wavelet center
fc = mahotas.wavelet_center(f)

# showing image
print("Image with wavelet center")
imshow(fc)
show()
