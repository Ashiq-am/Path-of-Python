# importing Image class from PIL package
from PIL import Image

# opening a singleband image
im = Image.open(r"C:\Users\Admin\Pictures\singleband.png")

# split() method
# this will split the image in individual bands
# and return a tuple (of 1 element for singleband)
im1 = Image.Image.split(im)

# showing image
im1[0].show()
