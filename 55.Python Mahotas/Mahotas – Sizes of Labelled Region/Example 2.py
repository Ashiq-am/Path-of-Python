# importing required libraries
import mahotas as mh
import numpy as np
from pylab import imshow, show

# creating region
# numpy.ndarray
regions = np.zeros((10, 10), bool)

# setting 1 value to the region
regions[:3, :3] = 1
regions[6:, 6:] = 1

# getting labelled function
labelled, nr_objects = mh.label(regions)

# showing the image with interpolation = 'nearest'
imshow(labelled, interpolation='nearest')
show()

# getting sizes of labelled region
sizes = mh.labelled.labelled_size(labelled)

# printing sizes
for i in range(len(sizes)):
    print("Size of region " + str(i) + " : " + str(sizes[i]))

