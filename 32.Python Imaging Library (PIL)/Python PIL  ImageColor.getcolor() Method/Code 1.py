

# importing Image module from PIL package
from PIL import Image, ImageColor

# using getcolor
im = ImageColor.getcolor("orange", "L")
print(im)

im1 = ImageColor.getcolor("red", "L")
print(im1)
