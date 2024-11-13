# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating a image1 object
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPg")

# applying equalize method
im2 = ImageOps.equalize(im1, mask=None)

im2.show()
