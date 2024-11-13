# importing required libraries
import mahotas
import mahotas.demos
import numpy as np
from pylab import imshow, show

# getting nuclear image
nuclear = mh.demos.nuclear_image()


# filtering the image
nuclear = nuclear[:, :, 0]

print("Image with filter")
# showing the image
imshow(nuclear)
show()

# setting gaussian filter
nuclear = mahotas.gaussian_filter(nuclear, 35)

print("Image with gaussian filter")
# showing the gaussian filter
imshow(nuclear)
show()
