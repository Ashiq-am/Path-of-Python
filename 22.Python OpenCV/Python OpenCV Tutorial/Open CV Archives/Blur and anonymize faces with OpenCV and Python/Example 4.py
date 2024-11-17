for x, y, w, h in face:

	# draw a border around the detected face.
	# (here border color = green, and thickness = 3)
	image = cv2.rectangle(frame, (x, y),
						(x+w, y+h),
						(0, 255, 0), 3)
