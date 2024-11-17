# Import OpenCV library
import cv2

# Read four Images
img1 = cv2.imread("Documents/geekslogo.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("Documents/geekslogo2.png", cv2.IMREAD_COLOR)
img3 = cv2.imread("Documents/geekslogo3.png", cv2.IMREAD_COLOR)
img4 = cv2.imread("Documents/geekslogo4.png", cv2.IMREAD_COLOR)


# Display images using imshow() function
cv2.imshow("I1", img1)
cv2.imshow("I2", img2)
cv2.imshow("I3", img3)
cv2.imshow("I4", img4)

# Move widow to (10,50) position
# using moveWindow() function
cv2.moveWindow("I1", 10, 50)
cv2.moveWindow("I2", 650, 50)
cv2.moveWindow("I3", 10, 500)
cv2.moveWindow("I4", 650, 500)

# Wait for user to press any key
cv2.waitKey(0)

# Close all opened windows
cv2.destroyAllWindows()
