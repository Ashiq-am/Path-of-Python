# importing required libraries
import mahotas as mh
import numpy as np
from pylab import imshow, show

# creating region
# numpy.ndarray
regions = np.zeros((10, 10), bool)

# setting 1 value to the region
regions[1, :2] = 1
regions[5:8, 6: 8] = 1
regions[8, 0] = 1

# getting labeled function
labeled, nr_objects = mh.label(regions)

# showing the image with interpolation = 'nearest'
print("Image")
imshow(labeled, interpolation='nearest')
show()

# getting edges
dog = mahotas.dog(labeled)

# showing image
print("Edges using DoG algo")
imshow(dog)
show()
