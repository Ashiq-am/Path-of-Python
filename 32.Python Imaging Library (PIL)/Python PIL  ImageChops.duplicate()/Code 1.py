## Importing Image and ImageChops module from PIL package
from PIL import Image, ImageChops

# creating a image1 object
im1 = Image.open(r"C:\Users\System-Pc\Desktop\leave.jpg")

# applying duplicate method
im3 = ImageChops.duplicate(im1)

im3.show()
