# import the image
from PIL import Image

# open the image
catIm = Image.open('D:/cat.jpg')

# print the format description of the image
print(catIm.format_description)
