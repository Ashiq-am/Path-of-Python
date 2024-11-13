# Importing Image module from PIL package
from PIL import Image

# creating a image1 object and convert it to mode 'P'
im1 = Image.open(r"C:\Users\sadow984\Desktop\i2.PNG").convert('L')

# creating a image2 object and convert it to mode 'P'
im2 = Image.open(r"C:\Users\sadow984\Desktop\c2.PNG").convert('L')

# alpha is 0.0, a copy of the first image is returned
im3 = Image.blend(im1, im2, 0.0)

# to show specified image
im3.show()
