

# importing Image class from PIL package
from PIL import Image

# creating a object
image = Image.open(r"C:\Users\System-Pc\Desktop\python.png")
MAX_SIZE = (100, 100)

image.thumbnail(MAX_SIZE)

# creating thumbnail
image.save('pythonthumb.png')
image.show()
