# Importing Image module from PIL package
from PIL import Image

# creating a image1 object and converting it to mode 'L'
im1 = Image.open(r"C:\Users\sadow984\Desktop\c2.PNG").convert('L')

# creating a image2 object and converting it to mode 'L'
im2 = Image.open(r"C:\Users\sadow984\Desktop\i2.PNG").convert('L')

# creating a mask image object and converting it to mode 'L'
mask = Image.open(r"C:\Users\sadow984\Desktop\i3.PNG").convert('L')

# compositing all the thre images
im3 = Image.composite(im1, im2, mask)

# to show specified image
im3.show()
