# Apply the Component analysis function
analysis = cv2.connectedComponentsWithStats(threshold,
											4,
											cv2.CV_32S)
(totalLabels, label_ids, values, centroid) = analysis

# Initialize a new image to
# store all the output components
output = np.zeros(gray_img.shape, dtype="uint8")
