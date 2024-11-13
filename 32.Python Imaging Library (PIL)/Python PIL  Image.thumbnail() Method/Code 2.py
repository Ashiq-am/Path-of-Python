

# importing Image class from PIL package
from PIL import Image

# creating a object
image = Image.open(r"C:\Users\System-Pc\Desktop\house.jpg")
MAX_SIZE = (500, 500)

image.thumbnail(MAX_SIZE)

# creating thumbnail
image.save('pythonthumb2.jpg')
image.show()
