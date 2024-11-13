# importing required libraries
import numpy as np
import mahotas
from pylab import imshow, show

# loading image
img = mahotas.imread('dog_image.png')

# filtering the image
img = img[:, :, 0]

print("Image with filter")
# showing the image
imshow(img)
show()

# getting mean value
mean = img.mean()

# printing mean value
print("Mean Value for 0 channel : " + str(mean))
