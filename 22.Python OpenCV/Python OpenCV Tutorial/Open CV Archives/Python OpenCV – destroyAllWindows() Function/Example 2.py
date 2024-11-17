# importing cv2 module
import cv2

# read the image
img = cv2.imread("gfg_logo.png")

# showing the images
cv2.imshow('P', img)
cv2.imshow('Q', img)

# Destroying All the windows
cv2.destroyAllWindows()

# using the wait key function to delay
# the closing of windows till any ke is pressed
cv2.waitKey(0)
