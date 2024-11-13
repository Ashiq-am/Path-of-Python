# import required modules
import cv2
import matplotlib.pyplot as plt

# read the image
image = cv2.imread('gfg.png')

# convert color image into grayscale image
img1 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# plot that grayscale image with Matplolib
# cmap stands for colormap
plt.imshow(img1, cmap='gray')

# display that image
plt.show()
