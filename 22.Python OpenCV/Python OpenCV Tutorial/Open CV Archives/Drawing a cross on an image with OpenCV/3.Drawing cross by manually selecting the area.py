# Importing the modules
import cv2
import numpy

# Reading the image
image = cv2.imread('image.png')

# Function to manually select the area
r = cv2.selectROI("select the area", image)

# Calculating the coordinates with the coordinates
# returned by the function
opposite_x = int(r[2]) - int(r[0])
bottom_y = int(r[1]) + (int(r[3]) - int(r[1]))

# Drawing the cross by the calcullated and
# obtained coordinates
cv2.line(image, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (0, 0, 255), 5)
cv2.line(image, (opposite_x, int(r[1])), (int(r[0]), bottom_y), (0, 0, 255), 5)

# Showing the image
cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
