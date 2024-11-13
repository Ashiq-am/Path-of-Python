# importing various libraries
import numpy as np
import mahotas
import mahotas.demos
from mahotas.thresholding import soft_threshold
from pylab import imshow, show
from os import path

# loading image
f = mahotas.demos.load('luispedro', as_grey = True)



# Transform using D8 Wavelet to obtain transformed image t
t = mahotas.daubechies(f, 'D8')

# Discard low-order bits:
t /= 8
t = t.astype(np.int8)


# showing transformed image
print("Transformed Image")
imshow(t)
show()


# reconstructed image
r = mahotas.idaubechies(t, 'D8')

# showing image
print("Reconstructed Image")
imshow(r)
show()
