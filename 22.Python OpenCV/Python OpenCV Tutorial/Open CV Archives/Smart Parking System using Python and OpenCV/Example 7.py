while video.isOpened():
    Spots.location = 0
    source, image = video.read()

    if not source:
        break

    height, width, layers = image.shape
    image = cv2.resize(image, (int(width * 0.35), int(height * 0.35)))

    min_pix = cv2.getTrackbarPos('Min pixels', 'parameters')
    max_pix = cv2.getTrackbarPos('Max pixels', 'parameters')
    low_threshold = cv2.getTrackbarPos('Threshold1', 'parameters')
    high_threshold = cv2.getTrackbarPos('Threshold2', 'parameters')

    for i in range(roi_data.shape[0]):
        drawRectangle(image, roi_data.iloc[i, 0], roi_data.iloc[i, 1], roi_data.iloc[i, 2], roi_data.iloc[i, 3],
                      low_threshold, high_threshold, min_pix, max_pix)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, 'Available Spots: ' + str(Spots.location),
                (10, 30), font, 1, (0, 255, 0), 3)
    cv2.imshow('Frame', image)

    canny = cv2.Canny(image, low_threshold, high_threshold)
    cv2.imshow('Canny', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
