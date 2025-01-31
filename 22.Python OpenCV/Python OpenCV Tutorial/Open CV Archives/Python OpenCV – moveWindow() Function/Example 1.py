# Import OpenCV library
import cv2

# Read an Image
img = cv2.imread("Documents/geekslogo.png",
				cv2.IMREAD_COLOR)

# Display image using imshow() function
cv2.imshow("I2", img)

# Move widow to (10,50) position
# using moveWindow() function
cv2.moveWindow("I2", 10, 50)

# Wait for user to press any key
cv2.waitKey(0)

# Close all opened windows
cv2.destroyAllWindows()
