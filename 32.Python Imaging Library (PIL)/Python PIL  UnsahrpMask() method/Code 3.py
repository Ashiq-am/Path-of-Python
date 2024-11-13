# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPG")

# applying the unsharpmask method
im2 = im1.filter(ImageFilter.UnsharpMask(radius=5, percent=500, threshold=10))

im2.show()
