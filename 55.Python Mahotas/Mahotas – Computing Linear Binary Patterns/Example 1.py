# importing various libraries
import mahotas
import mahotas.demos
import mahotas as mh
import numpy as np
from pylab import imshow, show
import matplotlib.pyplot as plt

# loading nuclear image
nuclear = mahotas.demos.nuclear_image()

# filtering image
nuclear = nuclear[:, :, 0]

# adding gaussian filter
nuclear = mahotas.gaussian_filter(nuclear, 4)

# setting threshold
threshed = (nuclear > nuclear.mean())

# making is labelled image
labeled, n = mahotas.label(threshed)

# showing image
print("Labelled Image")
imshow(labelled)
show()

# Computing Linear Binary Patterns
value = mahotas.features.lbp(labelled, 200, 5)

# showing histograph
plt.hist(value)
