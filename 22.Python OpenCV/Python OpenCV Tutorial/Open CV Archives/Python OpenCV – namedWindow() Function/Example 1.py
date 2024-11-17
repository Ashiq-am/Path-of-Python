# Python program to explain cv2.namedWindow() method

# Importing OpenCV
import cv2

# Path to image in local directory
path = 'C:/Users/art/OneDrive/Desktop/geeks.png'

# Using cv2.imread() to read an image in default mode
image = cv2.imread(path)

# Using namedWindow()
# A window with 'Display' name is created
# with WINDOW_AUTOSIZE, window size is set automatically
cv2.namedWindow("Display", cv.WINDOW_AUTOSIZE)

# using cv2.imshow() to display the image
cv2.imshow('Display', image)

# Waiting 0ms for user to press any key
cv2.waitKey(0)

# Using cv2.destroyAllWindows() to destroy
# all created windows open on screen
cv2.destroyAllWindows()
