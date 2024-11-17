while True:
	# reading the cap object for a single frame of video
	ret, frame = cap.read()
	# for displaying the frame read from cap object
	cv2.imshow("frame", frame)

	# using the VideoWriter object output for writing the
	# frame into the output video
	output.write(frame)

	# waitKey specifies the value in millisecond
	# for which a particular frame will be shown
	k = cv2.waitKey(24)

	# if 'q' is pressed then above while loop will
	# break and video reading and writing
	# process will stop
	if k == ord("q"):
		break
