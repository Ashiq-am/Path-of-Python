# importing pyplot from matplotlib
import matplotlib.pyplot as plt

# importing image from PIL
from PIL import Image

# reading image
img = Image.open('imR.png')

img.thumbnail((30, 30), Image.ANTIALIAS)

# bicubic used for interpolation
imgplot = plt.imshow(img, interpolation ='bicubic')
