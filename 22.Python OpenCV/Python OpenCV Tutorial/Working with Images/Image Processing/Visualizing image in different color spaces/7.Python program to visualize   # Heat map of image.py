# Python program to visualize
# Heat map of image

# Importing matplotlib and cv2
import matplotlib.pyplot as plt
import cv2

# reads the image
img = cv2.imread('g4g.png')

# plot heat map image
plt.imshow(img, cmap ='hot')
