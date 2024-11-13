# Importing Image and ImageChops module from PIL package
from PIL import Image, ImageChops

# creating a image1 object
im1 = Image.open(r"C:\Users\sadow984\Desktop\a2.PNG").convert("1")

# creating a image2 object
im2 = Image.open(r"C:\Users\sadow984\Desktop\x5.PNG").convert("1")

# applying logical_xor method
im3 = ImageChops.logical_xor(im1, im2)

im3.show()
