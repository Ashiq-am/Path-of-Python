# This will import Image and ImageChops modules
from PIL import Image, ImageChops

# Opening Images
im = Image.open(r"C:\Users\Admin\Pictures\download.png")
im2 = Image.open(r"C:\Users\Admin\Pictures\images.PNG")

# here getting absolute difference
# of image1 and image2
im3 = ImageChops.difference(im, im2)

# showing resultant image
im3.show()
