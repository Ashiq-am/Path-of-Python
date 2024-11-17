# Python program to explain cv2.copyMakeBorder() method

# importing cv2
import cv2

# path
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.copyMakeBorder() method
image = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT)

# Displaying the image
cv2.imshow(window_name, image)
