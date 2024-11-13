# Importing Image module from PIL package
from PIL import Image

# creating a image object
im1 = Image.open(r"C:\Users\sadow984\Desktop\i3.PNG")

# copying image to another image object
im2 = im1.copy()

# shows the original image
im1.show()
