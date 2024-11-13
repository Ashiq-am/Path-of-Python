

# importing image object from PIL
from PIL import Image

# creating an image object
im = Image.open(r"C:\Users\System-Pc\Desktop\ellipse1.png")
im1 = im.tobytes("xbm", "rgb")
img = Image.frombuffer("L", (10, 10), im1, 'raw', "L", 0, 1)

# creating list
img2 = list(img.getdata())
print(img2)
