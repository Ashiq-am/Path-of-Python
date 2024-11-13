# Importing Image and ImageChops module from PIL package
from PIL import Image, ImageChops

# creating a image1 object
im1 = Image.open(r"C:\Users\sadow984\Desktop\a2.PNG")

# creating a image2 object
im2 = Image.open(r"C:\Users\sadow984\Desktop\x5.PNG")

# applying add method
im3 = ImageChops.add(im1, im2, scale = 4.0, offset = 4)

im3.show()
