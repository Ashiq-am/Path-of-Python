

# importing Image class from PIL package
from PIL import Image

# creating a object
image = Image.open(r"C:\Users\System-Pc\Desktop\python.png")
image.load()
r, g, b, a = image.split()[1]

# merge funstion used
im1 = Image.merge('RGB', (r, g, b))
im1.show()
