# Importing Image and ImageChops module from PIL package
from PIL import Image, ImageChops

# creating a image3 object
im1 = Image.open(r"C:\Users\sadow984\Desktop\a2.PNG")

# creating a image4 object
im2 = Image.open(r"C:\Users\sadow984\Desktop\a3.PNG")

# applying multiply method
im3 = ImageChops.multiply(im1, im2)

im3.show()
