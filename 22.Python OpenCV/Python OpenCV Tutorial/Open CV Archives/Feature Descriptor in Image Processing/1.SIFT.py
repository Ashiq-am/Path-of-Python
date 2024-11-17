import cv2
# For SIFT to work, make sure you are using the OpenCV version <= 3.4.2.16
# Load an image
image = cv2.imread('rat.jpg')

# Resize the image using OpenCV's resize function
image = cv2.resize(image, (480, 480))

# Initialize the SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(image, None)

# Draw keypoints on the image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

cv2.imwrite('output_image.jpg', image_with_keypoints)
