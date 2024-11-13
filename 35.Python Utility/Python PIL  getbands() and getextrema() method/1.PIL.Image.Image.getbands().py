# Importing Image module from PIL package
from PIL import Image

# Opening a multiband image
im = Image.open(r"C:\Users\Admin\Pictures\images.png")

# This returns the bands used in im (image)
im1 = Image.Image.getbands(im)

print("Multiband image", im1)

# Opening a single band image
im2 = Image.open(r"C:\Users\Admin\Pictures\singleband.png")

# This returns the band used in im2
im3 = Image.Image.getbands(im2)

print("Single band image", im3)
