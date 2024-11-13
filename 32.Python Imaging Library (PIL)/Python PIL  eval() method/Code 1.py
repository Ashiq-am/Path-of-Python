

# Importing Image module from PIL package
from PIL import Image

# creating a image object
im2 = Image.open(r"C:\Users\System-Pc\Desktop\lion.PNG")

# applying the eval method
im3 = Image.eval(im2, (lambda x: 254 - x * 15))

im3.show()
