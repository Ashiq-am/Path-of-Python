# importing required libraries
import mahotas as mh
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

# setting image threshold
nuclear = (nuclear < nuclear.mean())

print("Image with threshold")
# showing the threshold image
imshow(nuclear)
show()
