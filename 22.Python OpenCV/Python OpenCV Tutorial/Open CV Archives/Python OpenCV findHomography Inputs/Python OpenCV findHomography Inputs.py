import cv2
import numpy as np

# Define source and destination points
srcPoints = np.array([[100, 100], [150, 100], [150, 150], [100, 150]], dtype=np.float32)
dstPoints = np.array([[200, 200], [250, 200], [250, 250], [200, 250]], dtype=np.float32)

# Compute homography matrix
H, mask = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)

# Print the resulting homography matrix
print("Homography Matrix:")
print(H)
