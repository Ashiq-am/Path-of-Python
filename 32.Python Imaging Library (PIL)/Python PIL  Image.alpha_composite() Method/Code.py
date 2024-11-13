
# importing image class from PIL package
from PIL import Image

# creating image object
img1 = Image.open(r"C:\Users\System-Pc\Desktop\home.png")

# creating image2 object having alpha
img2 = Image.open(r"C:\Users\System-Pc\Desktop\python.png")
img2 = img2.resize(img1.size)

# using alpha_composite
im3 = Image.alpha_composite(img1, img2)
im3.show()
