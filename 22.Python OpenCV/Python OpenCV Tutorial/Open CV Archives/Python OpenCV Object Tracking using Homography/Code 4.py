# maintaining list of index of descriptors
# in query descriptors
query_pts = np.float32([kp_image[m.queryIdx]
				.pt for m in good_points]).reshape(-1, 1, 2)

# maintaining list of index of descriptors
# in train descriptors
train_pts = np.float32([kp_grayframe[m.trainIdx]
				.pt for m in good_points]).reshape(-1, 1, 2)

# finding perspective transformation
# between two planes
matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)

# ravel function returns
# contiguous flattened array
matches_mask = mask.ravel().tolist()
