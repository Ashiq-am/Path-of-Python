# Python program to compute and visualize the
# histogram of Green channel of image

matplotlib
inline

# importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading the input image
img = cv2.imread('mountain.jpg')

# computing the histogram of the green channel of the image
hist = cv2.calcHist([img],[1],None,[256],[0,256])

# plot the above computed histogram
plt.plot(hist, color='g')
plt.title('Image Histogram For Green Channel GFG')
plt.show()
