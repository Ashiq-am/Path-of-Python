# Importing Image module from PIL package
from PIL import Image

# creating a image1 object and converting it to mode 'L'
mask = Image.open(r"C:\Users\sadow984\Desktop\i3.PNG").convert('L')
mask.show()
