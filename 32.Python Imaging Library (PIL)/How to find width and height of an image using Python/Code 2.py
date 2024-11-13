# import required module
from PIL import Image

# get image
filepath = "geeksforgeeks.png"
img = Image.open(filepath)

# get width and height
width,height = img.size

# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)
