# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance

# Opening Image
im = Image.open(r"geek.jpg")

# Creating object of Contrast class
im3 = ImageEnhance.Contrast(im)

# showing resultant image
im3.enhance(5.0).show()
