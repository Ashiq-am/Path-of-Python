for pair in POSE_PAIRS:
	partA = pair[0]
	partB = pair[1]

	if points[partA] and points[partB]:
		cv2.line(frameCopy, points[partA], points[partB], (0, 255, 0), 3)
