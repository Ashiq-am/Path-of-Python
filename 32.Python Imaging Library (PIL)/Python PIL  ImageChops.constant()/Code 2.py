
# importing image object from PIL
from PIL import Image, ImageChops

# creating an image object
img = Image.open(r"C:\Users\System-Pc\Desktop\rose.jpg")
img1 = ImageChops.constant(img, 200)

img1.show()
