# This will import Image and ImageChops modules
from PIL import Image, ImageChops

# Opening Images
im = Image.open(r"C:\Users\Admin\Pictures\download.png")
im2 = Image.open(r"C:\Users\Admin\Pictures\images.PNG")

# here adding image1 and image2
im3 = ImageChops.add_modulo(im, im2)

# showing resultant image
im3.show()
