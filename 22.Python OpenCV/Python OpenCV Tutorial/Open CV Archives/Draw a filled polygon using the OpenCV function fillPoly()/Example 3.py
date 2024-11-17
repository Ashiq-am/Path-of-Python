# Import necessary libraries
import cv2
import numpy as np

# Read an image
img = cv2.imread("Documents/Person_Image.jpg",
				cv2.IMREAD_COLOR)

# Define an array of endpoints of Rectangle
points = np.array([[300, 180], [400, 180],
				[400, 280], [300, 280]])

# Use fillPoly() function and give input as image,
# end points,color of polygon
# Here color of polygon will be red
cv2.fillPoly(img, pts=[points], color=(0, 0, 255))

# Displaying the image
cv2.imshow("Rectangle", img)

# wait for the user to press any key to exit window
cv2.waitKey(0)

# Closing all open windows
cv2.destroyAllWindows()
