# import the Image module
from PIL import Image

# Open the image
catIm = Image.open('D:/cat.jpg')

# print the filename
print(catIm.filename)
