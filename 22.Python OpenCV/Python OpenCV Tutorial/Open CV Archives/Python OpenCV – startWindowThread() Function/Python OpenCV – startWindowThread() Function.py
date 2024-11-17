# Python program for OpenCV
# startWindowThread() function

# Import the library OpenCV
import cv2

# Read the image
img = cv2.imread("gfg_black.png")

# Use high GUI windows
cv2.startWindowThread()

# Name the GUI app
cv2.namedWindow("preview", cv2.WINDOW_NORMAL)

# Display the image on GUI app
cv2.imshow("preview", img)

# Make Python sleep for unlimited time
cv2.waitKey(0)
