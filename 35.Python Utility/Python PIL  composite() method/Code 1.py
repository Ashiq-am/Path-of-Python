# Importing Image module from PIL package
from PIL import Image

# creating a image1 object and converting it to mode 'L'
im1 = Image.open(r"C:\Users\sadow984\Desktop\c2.PNG").convert('L')

im1.show()
