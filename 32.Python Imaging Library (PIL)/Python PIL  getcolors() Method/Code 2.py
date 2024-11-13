

# importing Image module from PIL package
from PIL import Image

# opening a image
im = Image.open(r"C:\Users\System-Pc\Desktop\new.jpg").convert("L")

# getting colors
# multiband images (RBG)
im1 = Image.Image.getcolors(im)

print(im1)
