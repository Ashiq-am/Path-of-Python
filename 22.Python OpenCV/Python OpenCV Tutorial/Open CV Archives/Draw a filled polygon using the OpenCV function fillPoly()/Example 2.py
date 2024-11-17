# Import necessary libraries
import cv2
import numpy as np

# Read an image
img = cv2.imread("image.png")

# Define an array of endpoints of Hexagon
points = np.array([[220, 120], [130, 200], [130, 300],
				[220, 380], [310, 300], [310, 200]])

# Use fillPoly() function and give input as image,
# end points,color of polygon
# Here color of polygon will be green
cv2.fillPoly(img, pts=[points], color=(0, 255, 0))

# Displaying the image
cv2.imshow("Hexagon", img)

# wait for the user to press any key to
# exit window
cv2.waitKey(0)

# Closing all open windows
cv2.destroyAllWindows()
