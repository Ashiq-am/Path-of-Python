

# importing image class from PIL package
from PIL import Image

# creating image object
img = Image.open(r"C:\Users\System-Pc\Desktop\scene4.jpg")

# using convert method for img1
img1 = img.convert("L")
img1.show()

# using convert method for img2
img2 = img.convert("1")
img2.show()
