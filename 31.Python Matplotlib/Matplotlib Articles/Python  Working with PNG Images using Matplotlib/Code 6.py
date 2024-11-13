# importing PIL and matplotlib
from PIL import Image
import matplotlib.pyplot as plt

# reading image
img = Image.open('imR.png')

img.thumbnail((30, 30), Image.ANTIALIAS)

# sinc used for interpolation
imgplot = plt.imshow(img, interpolation ='sinc')
