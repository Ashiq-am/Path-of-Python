# import Image module
from PIL import Image

# open the image
Image1 = Image.open('D:/cat.jpg')

# crop the image
croppedIm = Image1.crop((130, 50, 250, 150))

# show the image
croppedIm.show()
