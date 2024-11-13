# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os

# getting disk of given radius
disk = mahotas.disk(10)

# showing disk image
imshow(disk)
show()
