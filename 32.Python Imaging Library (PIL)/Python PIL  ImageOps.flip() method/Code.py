# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps

# creating a image1 object
im1 = Image.open(r"C:\Users\System-Pc\Desktop\a.JPG")

# applying flip method
im2 = ImageOps.flip(im1)

im2.show()
