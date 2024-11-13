# Python program to read
# image using PIL module

# importing PIL
from PIL import Image

# Read image
img = Image.open('g4g.png')

# Output Images
img.show()

# prints format of image
print(img.format)

# prints mode of image
print(img.mode)
