# importing cv2 module
import cv2

# read the image
img = cv2.imread("gfg_logo.png")

# showing the images
cv2.imshow('P', img)
cv2.imshow('Q', img)

# Destroying the window named P before
# calling the waitKey() function
cv2.destroyWindow('P')

# using the wait key function to delay the
# closing of windows till any ke is pressed
cv2.waitKey(0)
