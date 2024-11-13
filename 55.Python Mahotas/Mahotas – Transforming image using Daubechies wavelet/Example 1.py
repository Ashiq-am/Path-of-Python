# importing various libraries
import numpy as np
import mahotas
import mahotas.demos
from mahotas.thresholding import soft_threshold
from matplotlib import pyplot as plt
from os import path

# loading image
f = mahotas.demos.load('luispedro', as_grey = True)

# making ply gray
plt.gray()

# showing image
print("Image")
plt.imshow(f)
plt.show()

# Transform using D8 Wavelet to obtain transformed image t
t = mahotas.daubechies(f, 'D8')

# showing transformed image
print("Transformed Image")
plt.imshow(t)
plt.show()
