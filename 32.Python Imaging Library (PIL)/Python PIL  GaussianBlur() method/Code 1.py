# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"C:\Users\System-Pc\Desktop\leave.JPG")

# applying the Gaussian Blur filter
im2 = im1.filter(ImageFilter.GaussianBlur(radius = 5))

im2.show()
