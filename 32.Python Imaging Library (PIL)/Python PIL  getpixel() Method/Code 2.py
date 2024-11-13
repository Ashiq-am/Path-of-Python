# Importing Image from PIL package
from PIL import Image

# creating a image object
im = Image.open(r"C:\Users\System-Pc\Desktop\leave.jpg")
px = im.load()
print (px[4, 4])
px[4, 4] = (0, 0, 0)
print (px[4, 4])
cordinate = x, y = 180, 79

# using getpixel method
print (im.getpixel(cordinate))
