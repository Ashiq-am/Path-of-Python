# Python program to read image as GrayScale

# Importing cv2 module
import cv2

# Reads image as gray scale
img = cv2.imread('g4g.png', 0)

# We can alternatively convert
# image by using cv2color
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shows the image
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
