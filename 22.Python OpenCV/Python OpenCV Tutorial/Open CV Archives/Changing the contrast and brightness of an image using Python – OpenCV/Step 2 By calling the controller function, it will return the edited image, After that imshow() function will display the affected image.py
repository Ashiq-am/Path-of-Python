def BrightnessContrast(brightness=0):
    # getTrackbarPos returns the
    # current position of the specified trackbar.
    brightness = cv2.getTrackbarPos('Brightness',
                                    'GEEK')

    contrast = cv2.getTrackbarPos('Contrast',
                                  'GEEK')

    effect = controller(img,
                        brightness,
                        contrast)

    # The function imshow displays
    # an image in the specified window
    cv2.imshow('Effect', effect)
