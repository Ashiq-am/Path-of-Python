# importing required libraries
import mahotas as mh
import mahotas.demos
import numpy as np
from pylab import imshow, show

# getting nuclear image
nuclear = mh.demos.nuclear_image()

print("Original Image i.e without filter")
# show the original image
imshow(nuclear)
show()

# filtering the image
nuclear = nuclear[500:, 500:, :]

print("Image with filter")
# showing the image
imshow(nuclear)
show()
