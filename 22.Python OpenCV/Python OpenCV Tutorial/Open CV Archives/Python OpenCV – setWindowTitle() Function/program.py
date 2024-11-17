# importing cv2 module
import cv2

# read the image
img = cv2.imread("gfg_logo.png")

# showing the image
cv2.imshow('gfg', img)

# Setting the windows title to "Hello!"
# using setWindowTitle method
cv2.setWindowTitle('gfg', 'Hello!')

# waiting using waitKey method
cv2.waitKey(0)
