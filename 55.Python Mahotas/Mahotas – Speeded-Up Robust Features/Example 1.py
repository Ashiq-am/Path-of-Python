# importing various libraries
import mahotas
import mahotas.demos
import mahotas as mh
import numpy as np
from pylab import imshow, show
from mahotas.features import surf

# loading nuclear image
nuclear = mahotas.demos.nuclear_image()

# filtering image
nuclear = nuclear[:, :, 0]

# adding gaussian filter
nuclear = mahotas.gaussian_filter(nuclear, 4)

# showing image
print("Image")
imshow(nuclear)
show()


# getting Speeded-Up Robust Features
spoints = surf.surf(nuclear)
print("No of points: {}".format(len(spoints)))
