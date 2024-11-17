import cv2
from google.colab.patches import cv2_imshow
# Load the images
img1 = cv2.imread('image1.png', 0)
img2 = cv2.imread('image2.png', 0)

# Detect keypoints and descriptors using ORB
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Draw keypoints
img1_kp = cv2.drawKeypoints(img1, kp1, None, color=(0, 255, 0))
img2_kp = cv2.drawKeypoints(img2, kp2, None, color=(0, 255, 0))

# Display keypoints
cv2_imshow(img1_kp)
cv2_imshow(img2_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()
