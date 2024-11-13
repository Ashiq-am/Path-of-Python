# importing required libraries
import numpy as np
import mahotas
import mahotas.demos
from mahotas.thresholding import soft_threshold
from matplotlib import pyplot as plt
from os import path

# loading image as grey
f = mahotas.demos.load('luispedro', as_grey = True)

# making plt grey
plt.gray()

# showing image
print("Image")
plt.imshow(f)
plt.show()

# cropping image
f = f[50:200, 20: 250]


# Show the image
print("Cropped Image")
plt.imshow(f)
plt.show()
