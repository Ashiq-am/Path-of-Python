# Importing Image from PIL package
from PIL import Image

# creating a image object
image = Image.open(r'C:\Users\System-Pc\Desktop\python.png')

width, height = image.size

for x in range(height):
    image.putpixel((x, x), (0, 0, 0, 255))

image.show()
