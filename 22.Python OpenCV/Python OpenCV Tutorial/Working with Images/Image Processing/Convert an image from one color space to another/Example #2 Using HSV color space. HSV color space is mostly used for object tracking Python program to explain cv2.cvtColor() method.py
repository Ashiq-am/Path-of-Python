# Python program to explain cv2.cvtColor() method

# importing cv2
import cv2

# path
path = r'C:\Users\Administrator\Desktop\geeks.png'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2HSV color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )

# Displaying the image
cv2.imshow(window_name, image)
