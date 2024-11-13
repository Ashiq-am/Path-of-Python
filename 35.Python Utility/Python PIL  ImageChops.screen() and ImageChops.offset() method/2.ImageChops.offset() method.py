# This will import Image and ImageChops modules
from PIL import Image, ImageChops

# Opening Images
im = Image.open(r"C:\Users\Admin\Pictures\images.png")
im2 = Image.open(r"C:\Users\Admin\Pictures\download.PNG")

# Here, xoffset is given 100
# yoffset wil automaticallly set to 100
im3 = ImageChops.offset(im, 140)

# showing resultant image
im3.show()
