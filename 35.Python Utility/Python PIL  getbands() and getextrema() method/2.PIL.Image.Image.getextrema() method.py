# importing Image module from PIL package
from PIL import Image

# opening a multiband image
im = Image.open(r"C:\Users\Admin\Pictures\download.png")

# getting maximum and minimum pixels of
# multiband images (RBG)
im1 = Image.Image.getextrema(im)

print("Multi band image ", im1)

# Opening a single band image
im2 = Image.open(r"C:\Users\Admin\Pictures\singleband.png")

# getting maximum and minimum pixels of
# single band image
im3 = Image.Image.getextrema(im2)

print("Single band image ", im3)
