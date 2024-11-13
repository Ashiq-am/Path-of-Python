# importing required libraries
import mahotas
import numpy as np
from pylab import imshow, show

# creating region
# numpy.ndarray
regions = np.zeros((10, 10), bool)

# setting 1 value to the region
regions[:3, :3] = 1
regions[6:, 6:] = 1

# getting labeled function
labeled, nr_objects = mahotas.label(regions)

# showing the image with interpolation = 'nearest'
imshow(labeled, interpolation='nearest')
show()

# random agaary of region shapes
array = np.random.random_sample(regions.shape)

# getting labeld max array
l_array = mahotas.labeled.labeled_max(array, labeled)

print("Labeled Max array :")
# printing the values
for i in range(len(l_array)):
    print("Region " + str(i) + " : " + str(l_array[i]))
