# Importing Image from PIL package
from PIL import Image

# creating a image object
image = Image.open(r'C:\Users\System-Pc\Desktop\ybear.jpg')

width, height = image.size

for x in range(height):
    image.putpixel((x, x), (10, 10, 10, 255))

image.show()
