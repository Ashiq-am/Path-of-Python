# Importing Image and ImageChops module from PIL package
from PIL import Image, ImageChops

# creating a image1 object
im1 = Image.open(r"C:\Users\sadow984\Desktop\a2.PNG")

# applying invert method
im3 = ImageChops.invert(im1)

im3.show()
