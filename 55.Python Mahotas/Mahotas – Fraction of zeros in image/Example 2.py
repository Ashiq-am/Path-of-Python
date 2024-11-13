# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show
import os


# loading image
img = mahotas.imread('dog_image.png')

# filtering image
img = img[:, :, 0]


# getting fraction of zeros in image
fraction = np.mean(img == 0)

print("Fraction of zeros in image: {0}".format(fraction))
imshow(img)
show()



# Transform using D8 Wavelet to obtain transformed image t
t = mahotas.daubechies(img, 'D8')

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
