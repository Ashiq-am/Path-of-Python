# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating a image1 object
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPg")

# applying autocontrast method
im2 = ImageOps.autocontrast(im1, cutoff=2, ignore=2)

im2.show()
