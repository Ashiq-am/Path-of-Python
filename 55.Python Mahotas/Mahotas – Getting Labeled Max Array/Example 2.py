# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show

# loading image
img = mahotas.imread('dog_image.png')

# filtering the image
img = img[:, :, 0]

# setting gaussian filter
gaussian = mahotas.gaussian_filter(img, 15)

# setting threshold value
gaussian = (gaussian > gaussian.mean())

# creating a labeled image
labeled, n_nucleus = mahotas.label(gaussian)

print("Labelled Image")
# showing the gaussian filter
imshow(labeled)
show()

# random agary of region shapes
array = np.random.random_sample(labeled.shape)

# getting labeld max array
l_array = mahotas.labeled.labeled_max(array, labeled)

print("Labeled Max array :")
# printing the values
for i in range(len(l_array)):
    print("Region " + str(i) + " : " + str(l_array[i]))
