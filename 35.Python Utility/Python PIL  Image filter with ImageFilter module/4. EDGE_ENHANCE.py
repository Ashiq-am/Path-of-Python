# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPG")

# applying the EDGE_ENHANCE filter
im2 = im1.filter(ImageFilter.EDGE_ENHANCE)

im2.show()
