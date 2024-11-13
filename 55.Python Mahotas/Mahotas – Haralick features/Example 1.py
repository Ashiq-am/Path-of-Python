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

# making is labeled image
labeled, n = mahotas.label(threshed)

# showing image
print("Labelled Image")
imshow(labeled)
show()

# getting haralick features
h_feature = mahotas.features.haralick(labelled)

# showing the feature
print("Haralick Features")
imshow(h_feature)
show()
