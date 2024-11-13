# import required libraries
from __future__ import print_function
from urllib2 import urlopen
from wand.image import Image

response = urlopen('https://media.geeksforgeeks.org/wp-content/uploads/geeksforgeeks-6.png')
try:

    # read image using Image() function
    img = Image(file=response)

    # print height of image
    print('Height =', img.height)

    # print width of image
    print('Width =', img.width)
finally:
    response.close()
