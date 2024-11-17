# Python program for setTrackbarMin()
# Python OpenCV

# Importing the libraries OpenCV and numpy
import cv2
import numpy

# Create a function 'nothing' for
# creating trackbar
def nothing(x):
	pass

# Creating a window with black image
img = numpy.zeros((300, 512, 3), numpy.uint8)
cv2.namedWindow('image')

# Creating trackbars for color change
cv2.createTrackbar('color_track', 'image', 0, 255, nothing)

# Setting minimum position of 'color_track'
# trackbar to 100
cv2.setTrackbarMin('color_track', 'image', 100)

# Create a loop for displaying image and
# trackbar
while(True):

	# Display the image
	cv2.imshow('image', img)

	# Create a button for pressing and changing
	# the window
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	# Get current positions of trackbar
	color = cv2.getTrackbarPos('color_track', 'image')

	# Display color mixture
	img[:] = [color]

# Close the window
cv2.destroyAllWindows()
