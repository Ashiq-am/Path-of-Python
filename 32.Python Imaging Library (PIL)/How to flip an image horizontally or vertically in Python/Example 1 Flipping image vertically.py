# importing PIL Module
from PIL import Image

# open the original image
original_img = Image.open("original.png")

# Flip the original image verticaly
vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save("vertical.png")

# close all our files object
original_img.close()
vertical_img.close()
