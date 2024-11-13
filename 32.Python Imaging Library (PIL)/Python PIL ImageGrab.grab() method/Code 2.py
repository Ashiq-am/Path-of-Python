# Importing Image and ImageGrab module from PIL package
from PIL import Image, ImageGrab

# creating an image object
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPG")

# using the grab method
im2 = ImageGrab.grab(bbox=(0, 0, 300, 300))

im2.show()
