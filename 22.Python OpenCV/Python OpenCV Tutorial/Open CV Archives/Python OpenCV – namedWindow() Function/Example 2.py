# Python Program to explain namedWindow() method

# Importing OpenCV
import cv2

# Path to image in local directory
path = 'C:/Users/art/OneDrive/Desktop/geeks.png'

# Using cv2.imread() to read an image in grayscale mode
image = cv2.imread(path, 0)

# Using namedWindow()
# A window with 'Display_Image' name is created
# with WINDOW_NORMAL allowing us to have random size
cv2.namedWindow("Display_Image", cv.WINDOW_NORMAL)

# Using cv2.imshow() to display the image
cv2.imshow('Display_Image', image)

# Waiting 0ms for user to press any key
cv2.waitKey(0)

# Using cv2.destroyAllWindows() to destroy
# all created windows open on screen
cv2.destroyAllWindows()
