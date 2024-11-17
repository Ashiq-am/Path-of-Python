while True:
    # Capture frame-by-frame
    _, img = video.read()
    img = cv2.flip(img, 1)

    # Find the hand with help of detector
    hand = detector.findHands(img, draw=False)

    # Here we take img by default if no hand found
    fing = cv2.imread("Put image path with 0 fingures up")
    if hand:

        # Taking the landmarks of hand
        lmlist = hand[0]
        if lmlist:

            # Find how many fingers are up
            # This function return list
            fingerup = detector.fingersUp(lmlist)

            # Change image based on
            # different-different conditions
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread("Put image path of 1\
				fingures up")
            if fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread("Put image path of 2\
				fingures up")
            if fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread("Put image path of\
				3 fingures up")
            if fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread("sPut image path \
				of 4 fingures up")
            if fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread("Put image path \
				of 4 fingures and thumbs up")
    # Resize the image
    fing = cv2.resize(fing, (220, 280))

    # Place the image in main frame
    img[50:330, 20:240] = fing

    # Display the resulting frame
    cv2.imshow("Video", img)
