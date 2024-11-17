# Python program for setTrackbarMax()
#Python OpenCV

# Importing the libraries OpenCV and numpy
import cv2
import numpy

# Create a function 'nothing' for creating trackbar
def nothing(x):
	pass

# Creating a window with black image
img = numpy.zeros((300, 512, 3), numpy.uint8)
cv2.namedWindow('image')

# Creating trackbars for red color change
cv2.createTrackbar('Red', 'image', 0, 255, nothing)

# Creating trackbars for Green color change
cv2.createTrackbar('Green', 'image', 0, 255, nothing)

# Creating trackbars for Blue color change
cv2.createTrackbar('Blue', 'image', 0, 255, nothing)

# Setting maximum values of green color trackbar
cv2.setTrackbarMax('Green', 'image', 100)

# Setting maximum values of red color trackbar
cv2.setTrackbarMax('Red', 'image', 200)

# Setting maximum values of blue color trackbar
cv2.setTrackbarMax('Blue', 'image', 150)

# Create a loop for displaying image and trackbar
while(True):

	# Display the image
	cv2.imshow('image', img)

	# Create a button for pressing and changing the window
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

	# Get current positions of red color trackbar
	red_color = cv2.getTrackbarPos('Red', 'image')

	# Get current positions of green color trackbar
	green_color = cv2.getTrackbarPos('Green', 'image')

	# Get current positions of blue color trackbar
	blue_color = cv2.getTrackbarPos('Blue', 'image')

	# Display color mixture
	img[:] = [blue_color, green_color, red_color]

# Close the window
cv2.destroyAllWindows()
