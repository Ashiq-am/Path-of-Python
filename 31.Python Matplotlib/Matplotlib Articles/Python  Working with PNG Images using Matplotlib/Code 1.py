# importing pyplot and image from matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img

# reading png image file
im = img.imread('imR.png')

# show image
plt.imshow(im)
