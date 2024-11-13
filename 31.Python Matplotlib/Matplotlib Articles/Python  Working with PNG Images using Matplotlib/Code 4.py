# importing PIL and matplotlib
from PIL import Image
import matplotlib.pyplot as plt

# reading png image file
img = Image.open('imR.png')

# resizing the image
img.thumbnail((50, 50), Image.ANTIALIAS)
imgplot = plt.imshow(img)
