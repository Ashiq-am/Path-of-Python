

# Importing Image module from PIL package
from PIL import Image

# creating a image object
img = Image.open(r"C:\Users\System-Pc\Desktop\tree.jpg")

# using tobytes
img.tobytes("xbm", "rgb")
print(img)
