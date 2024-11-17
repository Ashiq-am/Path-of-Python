import cv2

# read the image
img = cv2.imread("test.jpeg")
print(type(img))

# Check the shape of the input image
print("Shape of the image", img.shape)
