import cv2
import matplotlib.pyplot as plt

# reading image using the imread() function
imageread = cv2.imread('img1.jpeg')

# input image is converted to gray scale image
imagegray = cv2.cvtColor(imageread, cv2.COLOR_BGR2GRAY)

# using the SIRF algorithm to detect key
# points in the image
features = cv2.SIFT_create()

keypoints = features.detect(imagegray, None)

# drawKeypoints function is used to draw keypoints
output_image = cv2.drawKeypoints(imagegray, keypoints, 0, (0, 255, 0),
								flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

# displaying the image with keypoints as
# the output on the screen
plt.imshow(output_image)

# plotting image
plt.show()
