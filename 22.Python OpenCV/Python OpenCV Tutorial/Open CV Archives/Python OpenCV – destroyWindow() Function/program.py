# import cv2 library
import cv2

# Read an image
img = cv2.imread("Documents/Image3.jpg",
				cv2.IMREAD_COLOR)

# create two windows of images and
# give different window name to each
cv2.imshow("I1", img)
cv2.imshow("I2", img)

# we will wait for user to press any key
cv2.waitKey(0)

# after user pressed any key only 'I2' named
# window will be closed and another image
# remains as it is.
cv2.destroyWindow("I2")
