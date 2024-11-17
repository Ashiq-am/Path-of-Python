# Python program to explain cv2.resizeWindow() method

# Importing cv2
import cv2

# Path
path = 'C:/Users/art/OneDrive/Desktop/geeks.png'

# Reading an image in grayscale mode
image = cv2.imread(path, 0)

# Naming a window
cv2.namedWindow("Resize", cv2.WINDOW_NORMAL)


# Using resizeWindow()
cv2.resizeWindow("Resize", 700, 200)

# Displaying the image
cv2.imshow("Resize", image)
cv2.waitKey(0)
