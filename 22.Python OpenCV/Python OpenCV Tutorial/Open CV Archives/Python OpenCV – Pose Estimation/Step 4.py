H = out.shape[2]
W = out.shape[3]
# Empty list to store the detected keypoints
points = []
for i in range(len()):
	# confidence map of corresponding body's part.
	probMap = output[0, i, :, :]

	# Find global maxima of the probMap.
	minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

	# Scale the point to fit on the original image
	x = (frameWidth * point[0]) / W
	y = (frameHeight * point[1]) / H

	if prob > threshold:
		cv2.circle(frame, (int(x), int(y)), 15, (0, 255, 255),
				thickness=-1, lineType=cv.FILLED)
		cv2.putText(frame, "{}".format(i), (int(x), int(
			y)), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, lineType=cv2.LINE_AA)

		# Add the point to the list if the probability is greater than the threshold
		points.append((int(x), int(y)))
	else:
		points.append(None)

cv2.imshow("Output-Keypoints", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
