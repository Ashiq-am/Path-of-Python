utlis.initializeTrackbars()
count = 0

while True:

    success, img = cap.read()


    if success:
        print("Frame read successfully")
    else:
        print("Failed to read frame")
        break

    if not img.size:  # Check if the frame is empty
        print("Empty frame")
        continue
