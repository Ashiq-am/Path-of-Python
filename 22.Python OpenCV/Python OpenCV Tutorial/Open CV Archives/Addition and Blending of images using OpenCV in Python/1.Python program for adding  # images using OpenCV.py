# Python program for adding
# images using OpenCV

# import OpenCV file
import cv2

# Read Image1
mountain = cv2.imread('F:\mountain.jpg', 1)

# Read image2
dog = cv2.imread('F:\dog.jpg', 1)

# Add the images
img = cv2.add(mountain, dog)

# Show the image
cv2.imshow('image', img)

# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.distroyAllWindows()
