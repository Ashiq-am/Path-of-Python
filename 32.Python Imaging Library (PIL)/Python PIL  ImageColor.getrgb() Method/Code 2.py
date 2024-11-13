

# importing Image module from PIL package
from PIL import Image, ImageColor

# using getrgb
im = ImageColor.getrgb("blue")
print(im)

im1 = ImageColor.getrgb("yellow")
print(im1)
