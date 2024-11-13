

# importing Image class from PIL package
from PIL import Image

# creating a object
im = Image.open(r"C:\Users\System-Pc\Desktop\butter.png")

# using putalpha method
im.putalpha(1)

# show image object
im.show()
