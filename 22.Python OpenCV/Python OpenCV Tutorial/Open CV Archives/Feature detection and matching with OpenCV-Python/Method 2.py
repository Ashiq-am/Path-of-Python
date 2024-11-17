# Importing the libraries
import cv2
import numpy as np

# Reading the image and converting into B?W
image = cv2.imread("book.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying the function
corners = cv2.goodFeaturesToTrack(
	gray_image, maxCorners=50, qualityLevel=0.02, minDistance=20)
corners = np.float32(corners)

for item in corners:
	x, y = item[0]
	x = int(x)
	y = int(y)
	cv2.circle(image, (x, y), 6, (0, 255, 0), -1)

# Showing the image
cv2.imshow('good_features', image)
cv2.waitKey()
