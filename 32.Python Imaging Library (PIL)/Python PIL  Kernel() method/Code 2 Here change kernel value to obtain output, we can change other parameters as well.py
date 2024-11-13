# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"C:\Users\System-Pc\Desktop\leave.JPG")

# applying the Kernel filter
im2 = im1.filter(ImageFilter.Kernel((3, 3),
		(-1, -1, -1, -1, 11, -2, -2, -2, -2), 1, 0))

im2 = im2.show()
