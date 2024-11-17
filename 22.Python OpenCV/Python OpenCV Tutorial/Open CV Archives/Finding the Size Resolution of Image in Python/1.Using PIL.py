# importing the module
import PIL
from PIL import Image

# loading the image
img = PIL.Image.open("geeksforgeeks.png")

# fetching the dimensions
wid, hgt = img.size

# displaying the dimensions
print(str(wid) + "x" + str(hgt))
