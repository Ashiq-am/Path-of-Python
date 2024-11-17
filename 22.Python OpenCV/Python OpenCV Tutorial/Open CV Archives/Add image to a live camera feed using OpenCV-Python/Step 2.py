# Setup camera
cap = cv2.VideoCapture(0)

# While loop
while True:

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Show the captured image
    cv2.imshow('WebCam', frame)

    # wait for the key and come out of the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Discussed below
cv2.release()
cv2.destroyAllWindows()
