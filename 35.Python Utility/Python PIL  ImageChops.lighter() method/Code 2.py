# Importing Image and ImageChops module from PIL package
from PIL import Image, ImageChops

# creating a image1 object
im1 = Image.open(r"C:\Users\sadow984\Desktop\i3.PNG")

# creating a image2 object
im2 = Image.open(r"C:\Users\sadow984\Desktop\c1.PNG")

# applying lighter method
im3 = ImageChops.lighter(im2, im1)

im3.show()
