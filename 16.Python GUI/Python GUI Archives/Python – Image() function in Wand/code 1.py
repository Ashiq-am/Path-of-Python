# import required libraries
from __future__ import print_function
from wand.image import Image

# read image using Image() function
img = Image(filename ='koala.jpg')

# print height of image
print('height =', img.height)


# print width of image
print('width = ', img.width)
