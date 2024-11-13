# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance

# Opening Image
im = Image.open(r"C:\Users\Admin\Pictures\images.png")

# Creating object of Brightness class
im3 = ImageEnhance.Brightness(im)

# showing resultant image
im3.enhance(2.0).show()
