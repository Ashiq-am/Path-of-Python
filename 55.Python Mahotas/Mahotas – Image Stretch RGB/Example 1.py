# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np
import matplotlib.pyplot as plt

# loading image
img = mahotas.demos.load('lena')

print("Image")

# showing image
imshow(img)
show()

# stretching rgb image
new_img = mahotas.stretch_rgb(img)


# Stretched image
print("Stretched Image")
imshow(new_img)
show()
