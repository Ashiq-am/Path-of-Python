# importing cv2 module
import cv2

# read the image
img = cv2.imread("gfg_logo.png")

# showing the image
cv2.imshow('gfg', img)

# waiting using waitKey method
cv2.waitKey(5000)
