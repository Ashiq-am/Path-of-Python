import cv2

# Read Input Image
img = cv2.imread("test.jpeg")

# Check the type of read image
print(type(img))

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
