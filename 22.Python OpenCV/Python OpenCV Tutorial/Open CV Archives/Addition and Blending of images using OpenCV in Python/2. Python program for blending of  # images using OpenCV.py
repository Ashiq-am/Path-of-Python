# Python program for blending of
# images using OpenCV

# import OpenCV file
import cv2

# Read Image1
mountain = cv2.imread('F:\mountain.jpg', 1)

# Read image2
dog = cv2.imread('F:\dog.jpg', 1)

# Blending the images with 0.3 and 0.7
img = cv2.addWeighted(mountain, 0.3, dog, 0.7, 0)

# Show the image
cv2.imshow('image', img)

# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.distroyAllWindows()
