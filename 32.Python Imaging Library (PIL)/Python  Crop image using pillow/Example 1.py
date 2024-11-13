# import Image module
from PIL import Image

# open the image
Image1 = Image.open('D:/cat.jpg')

# crop the image
croppedIm = Image1.crop((130, 120, 200, 200))

# show the image
croppedIm.show()
