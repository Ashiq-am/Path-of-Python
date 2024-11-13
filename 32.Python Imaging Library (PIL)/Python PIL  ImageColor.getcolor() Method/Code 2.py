

# importing Image module from PIL package
from PIL import Image, ImageColor

# using getcolor
im = ImageColor.getcolor("pink", "L")
print(im)

im1 = ImageColor.getcolor("violet", "L")
print(im1)
