# Python program to explain cv2.resizeWindow() method

# Importing cv2
import cv2

# Path
path = 'C:/Users/art/OneDrive/Desktop/geeks.png'

# Reading an image in default mode
image = cv2.imread(path)

# Naming a window
cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)

# Using resizeWindow()
cv2.resizeWindow("Resized_Window", 300, 700)

# Displaying the image
cv2.imshow("Resized_Window", image)
cv2.waitKey(0)
