# Python program to visualize
# Spectral map of image

# Importing matplotlib and cv2
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('g4g.png')
plt.imshow(img, cmap ='nipy_spectral')
