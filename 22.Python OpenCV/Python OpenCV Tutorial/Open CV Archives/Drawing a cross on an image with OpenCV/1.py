# Importing the necessary libraries
import cv2
import numpy

# Reading the image
image = cv2.imread('image.png')

# Getting the height and width of the image
height = image.shape[0]
width = image.shape[1]

# Drawing the lines
cv2.line(image, (0, 0), (width, height), (0, 0, 255), 5)
cv2.line(image, (width, 0), (0, height), (0, 0, 255), 5)

# Showing the image
cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
