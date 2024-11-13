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

# getting labelled function
labelled, nr_objects = mahotas.label(regions)

print("Labelled Image")
# showing the image with interpolation = 'nearest'
imshow(labelled, interpolation ='nearest')
show()

# removing region
labelled2 = mahotas.labelled.remove_regions(labelled, 1, 1)


# showing the labelled image
print("Labelled Image with removed region")
imshow(labelled2)
show()
