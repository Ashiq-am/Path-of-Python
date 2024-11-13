# This will import Image and ImageChops modules
from PIL import Image, ImageChops

# Opening Images
im = Image.open(r"C:\Users\Admin\Pictures\images.png")
im2 = Image.open(r"C:\Users\Admin\Pictures\download.PNG")

# subtracting im and im2
im3 = ImageChops.subtract_modulo(image1 = im, image2 = im2)

# showing resultant image
im3.show()
