# Python program to change the ratio of height and
# width of an image
from PIL import Image

# Taking image as input
img = Image.open('logo.png')

# Getting height and width of the image
height = img.size[0]
width = img.size[1]

# Printing ratio before conversion
print('Ratio before conversion:', width/height)

# Changing the height and width of the image
width = width + 25
height = height - 25

# Resizing the image
img = img.resize((width ,height), Image.ANTIALIAS)

# Printing the ratio after conversion
print('Ratio after conversion:', width/height)

# Saving the resized image
img.save('Resized Image.png')
