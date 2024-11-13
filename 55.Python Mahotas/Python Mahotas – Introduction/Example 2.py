# importing required libraries
import pylab as p
import numpy as np
import mahotas

# creating numpy array of type bool
f = np.ones((256, 256), bool)

# setting false values
f[200:, 240:] = False
f[128:144, 32:48] = False

# f is basically True with the exception of two islands:
# one in the lower-right
# corner, another, middle-left

# creating a distance using numpy array
dmap = mahotas.distance(f)

# showing image
p.imshow(dmap)
p.show()
