# Importing Image module from PIL package
from PIL import Image

# creating a image object
im2 = Image.open(r"C:\Users\System-Pc\Desktop\eval2image.PNG")

# applying the eval method
im3 = Image.eval(im2, (lambda x: 240 - x * 12))

im3.show()
