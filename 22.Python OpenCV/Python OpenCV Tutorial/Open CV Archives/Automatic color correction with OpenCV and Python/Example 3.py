import cv2

# Load the image
img = cv2.imread('image.jpg')

# Apply a bilateral filter to the image
filtered = cv2.bilateralFilter(img, 15, 75, 75)

# Display the result
cv2.imshow('Color Corrected Image', filtered)
cv2.waitKey(0)
