# importing required libraries
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np

# loading image
img = mahotas.demos.load('lena')

# showing image
print("Image")
imshow(img)
show()

# getting infocusness of each pixel
focus = np.array([mahotas.sobel(t, just_filter = True) for t in img])

# showing focus pixel
print("Focus Image")
imshow(focus)
show()
