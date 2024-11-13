# import Image module
from PIL import Image

# open the image
catIm = Image.open('D:/cat.jpg')

# Display the dimensions of the image
print(catIm.size)
