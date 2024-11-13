# importing Image class from PIL package
from PIL import ImageChops, Image

# opening images to compare
im1 = Image.open(r"C:\Users\Admin\Pictures\geeks.png")
im2 = Image.open(r"C:\Users\Admin\Pictures\capture.png")

# Checking and returning a copy
# of image contating darker pixels
im = ImageChops.darker(im1, im2)

# showing image
im.show()
