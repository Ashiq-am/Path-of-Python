import cv2

cam = cv2.VideoCapture(0)
while True:
	_, frame = cam.read()
	cv2.imshow('Camera Feed', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cam.release()
