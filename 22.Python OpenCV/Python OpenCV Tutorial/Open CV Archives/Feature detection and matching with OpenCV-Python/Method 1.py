# Importing the libraries
import cv2
import numpy as np

# Reading the image and converting the image to B/W
image = cv2.imread('book.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = np.float32(gray_image)

# Applying the function
dst = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)

# dilate to mark the corners
dst = cv2.dilate(dst, None)
image[dst > 0.01 * dst.max()] = [0, 255, 0]

cv2.imshow('haris_corner', image)
cv2.waitKey()
