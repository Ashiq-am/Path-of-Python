# Importing the libraries
import cv2
import numpy

# Initiating the webcam
vid = cv2.VideoCapture(0)

# Capturing frames and showing as a video
while(True):
	ret, frame = vid.read()

	# Getting the width and height of the feed
	height = int(vid.get(4))
	width = int(vid.get(3))

	# Drawing cross on the webcam feed
	cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 5)
	cv2.line(frame, (width, 0), (0, height), (0, 0, 255), 5)

	# Showing the video
	cv2.imshow('LIVE', frame)

	# Making sure that we have a key to break the while loop
	# Which checks for the ascii value of the key pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# At last release the camera
vid.release()
cv2.destroyAllWindows()
