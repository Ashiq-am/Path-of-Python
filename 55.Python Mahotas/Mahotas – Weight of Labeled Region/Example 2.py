# importing required libraries
import mahotas as mh
import numpy as np
from pylab import imshow, show

# creating region
# numpy.ndarray
regions = np.zeros((10, 10), bool)

# setting 1 value in the region
regions[1, 1] = 1
regions[6, 6] = 1
regions[4, 4] = 1
regions[9, 9] = 1

# getting labeled function
labeled, nr_objects = mh.label(regions)

# showing the image with interpolation = 'nearest'
imshow(labeled, interpolation='nearest')
show()

# random agaary of region shapes
array = np.random.random_sample(regions.shape)

# getting sum i.e area
sums = mh.labeled_sum(array, labeled)

# printing the sums values
for i in range(len(sums)):
    print("Sum of region " + str(i) + " : " + str(sums[i]))
