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

# getting labeled function
labeled, nr_objects = mh.label(regions)

# showing the image with interpolation = 'nearest'
print("Binary Image")
imshow(labeled, interpolation='nearest')
show()

# getting edges using dog algo
dog = mahotas.dog(labeled)

# showing image
print("Edges using DoG algo")
imshow(dog)
show()
