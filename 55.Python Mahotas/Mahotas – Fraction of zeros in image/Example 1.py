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

# getting fraction of zeros in image
fraction = np.mean(f == 0)

print("Fraction of zeros in image: {0}".format(fraction))
imshow(f)
show()



# Transform using D8 Wavelet to obtain transformed image t
t = mahotas.daubechies(f, 'D8')

# Discard low-order bits:
t /= 8
t = t.astype(np.int8)


# getting fraction of zeros in image
fraction = np.mean(t == 0)

print("Fraction of zeros in transform (after division by 8): {0}".format(fraction))

# showing transformed image
print("Transformed Image")
imshow(t)
show()
