# Python program to explain cv2.transpose() method

# importing cv2
import cv2

# path
path = r'C:\Users\user\Desktop\geeks14.png'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.transpose() method
image = cv2.transpose(src)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
