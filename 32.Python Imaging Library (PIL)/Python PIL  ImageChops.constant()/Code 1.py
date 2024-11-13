
# importing image object from PIL
from PIL import Image, ImageChops

# creating an image object
img = Image.open(r"C:\Users\System-Pc\Desktop\TREE.JPG")
img1 = ImageChops.constant(img, 60)

img1.show()
