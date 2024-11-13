# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance

# Opening Image
im = Image.open(r"C:\Users\Admin\Pictures\images.png")

# Creating object of Color class
im3 = ImageEnhance.Color(im)

# showing resultant image
im3.enhance(0.0).show()
