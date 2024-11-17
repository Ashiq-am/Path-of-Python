# Perspective transform
M = cv2.getPerspectiveTransform(np.array(ordered_corners, dtype="float32"), destination_corners)
warped = cv2.warpPerspective(original_image, M, (maxWidth, maxHeight))
