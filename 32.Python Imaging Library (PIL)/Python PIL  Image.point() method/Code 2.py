

# importing Image class from PIL package
from PIL import Image

# creating a object
im = Image.open(r"C:\Users\System-Pc\Desktop\home.png")

# using point function
threshold = 120
im = im.point(lambda p: p > threshold and 255)
im.show()
