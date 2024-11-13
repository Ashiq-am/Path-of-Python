

# importing image object from PIL
from PIL import Image

# creating an image object
im = Image.open(r"C:\Users\System-Pc\Desktop\rose.jpg")
im1 = im.tobytes("xbm", "rgb")
img = Image.frombuffer("L", (4, 4), im1, 'raw', "L", 0, 1)

# creating list
img2 = list(img.getdata())
print(img2)
