video_capture = cv2.VideoCapture(0)
while True:
    # capture the latest frame from the video
    check, frame = video_capture.read()
