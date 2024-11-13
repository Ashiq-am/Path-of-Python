# importing various libraries
import mahotas
import mahotas.demos
import mahotas as mh
import numpy as np
from pylab import imshow, show

# loading nuclear image
nuclear = mahotas.demos.nuclear_image()

# filtering image
nuclear = nuclear[:, :, 0]

# adding gaussian filter
nuclear = mahotas.gaussian_filter(nuclear, 4)

# setting threshold
threshed = (nuclear > nuclear.mean())

# creating distance map
dmap = mahotas.distance(threshed)

print("Distance Map")
# showing image
imshow(dmap)
show()

# numpy ones array
Bc = np.ones((3, 2))

# getting maxima
maxima = mahotas.morph.regmax(dmap, Bc = Bc)

# showing image
print("Maxima")
imshow(maxima)
show()
