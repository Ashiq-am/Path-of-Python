# This will import Image and ImageChops modules
from PIL import Image, ImageEnhance

# Opening Image
im = Image.open(r"C:\Users\Admin\Pictures\images.png")

# Creating object of Sharpness class
im3 = ImageEnhance.Sharpness(im)

# showing resultant image
im3.enhance(-2.0).show()
