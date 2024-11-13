# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np
import matplotlib.pyplot as plt

# loading iamge
img = mahotas.demos.load('lena')

# filtering image
img = img.max(2)

print("Image")

# showing image
imshow(img)
show()

# strecting image
new_img = mahotas.stretch(img)

# Stretched image
print("Stretched Image")
imshow(new_img)
show()
