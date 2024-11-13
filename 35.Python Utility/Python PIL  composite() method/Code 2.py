# Importing Image module from PIL package
from PIL import Image

# creating a image1 object and converting it to mode 'L'
im2 = Image.open(r"C:\Users\sadow984\Desktop\i2.PNG").convert('L')
im2.show()
