

# importing image object from PIL
from PIL import Image

# creating an image object
im = Image.open(r"C:\Users\System-Pc\Desktop\rose.jpg")

# print the original image object
print(im)

# using draft function
# convert mode and size as well
im1 = im.draft("L", (im.width // 2, im.height // 2))
im2 = im1.decoderconfig, im1.mode, im.size, im1.tile
print(im1)
print(im2)

# show the converted image
im1.show()
