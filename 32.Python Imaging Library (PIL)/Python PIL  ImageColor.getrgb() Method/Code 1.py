

# importing Image module from PIL package
from PIL import Image, ImageColor

# using getrgb
im = ImageColor.getrgb("orange")
print(im)

im1 = ImageColor.getrgb("red")
print(im1)
