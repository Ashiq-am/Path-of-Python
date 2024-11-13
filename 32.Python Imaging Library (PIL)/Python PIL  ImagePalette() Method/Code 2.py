

# importing Image module from PIL package
from PIL import Image, ImagePalette

# opening a image
im = Image.open(r"C:\Users\System-Pc\Desktop\scene4.jpg")

# ImagePalette
im1 = ImagePalette.ImagePalette(mode ='RGB', palette = None, size = 0)
print(im1)
