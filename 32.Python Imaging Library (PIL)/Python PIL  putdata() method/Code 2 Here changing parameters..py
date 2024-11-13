

# from pure python list data
from PIL import Image

img = Image.new("L", (224, 224))
newdata = list(range(0, 256, 4)) * 224
img.putdata(newdata)
img.show()
