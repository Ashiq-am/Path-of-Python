# import Image module
from PIL import Image

# Open the image
catIm = Image.open('D:/cat.jpg')

# Create two different variables
# The first one will contain width and
# the second one will contain height
width, height = catIm.size

# Display height and width
print(height)
print(width)
