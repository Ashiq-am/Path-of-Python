# Importing Image module from PIL package
from PIL import Image

# creating a image object (main image)
im1 = Image.open(r"C:\Users\Admin\Pictures\network.PNG")

# creating a image object (image which is to be paste on main mage)
im2 = Image.open(r"C:\Users\Admin\Pictures\geeks.PNG")

# pasting im2 on im1
Image.Image.paste(im1, im2, (50, 125))

# to show specified image
im1.show()
