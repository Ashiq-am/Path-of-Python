# Importing Image module from PIL package
from PIL import Image

# creating a image object
im1 = Image.open(r"C:\Users\sadow984\Desktop\r1.PNG")

# get bands of image
im2 = im1.getbands()

# print band names.
print(im2)
