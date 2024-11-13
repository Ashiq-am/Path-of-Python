

# importing Image module from PIL package
from PIL import Image

# opening a image
im = Image.open(r"C:\Users\System-Pc\Desktop\python.png")

# use getpallete
im2 = im.getpalette()
print(im2)
