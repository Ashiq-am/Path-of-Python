# importing the modules needed
import cv2
import numpy as np

# Reading the image
image = cv2.imread('image.png')

# Creating the kernel(2d convolution matrix)
kernel2 = np.array([[-1, -1, -1],
					[-1, 8, -1],
					[-1, -1, -1]])

# Applying the filter2D() function
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

# Shoeing the original and output image
cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.destroyAllWindows()
