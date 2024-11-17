while True:
    success, img = cap.read()  # Read frame from camera
    allHands, img = detector.findHands(img)  # Find hands in the frame

    if len(allHands) == 0:
        lm_list, bbox_info = [], []
    else:
        # Find landmarks and bounding box info
        lm_list, bbox_info = allHands[0]['lmList'], allHands[0]['bbox']

    img = draw_buttons(img, button_list)  # Draw buttons on the frame

    # Check if landmarks (lmList) are detected
    if lm_list:
        for button in button_list:
            x, y = button.pos
            w, h = button.size

            # Check if index finger (lmList[8]) is within the button bounds
            if x < lm_list[8][0] < x + w and y < lm_list[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h),
                              (247, 45, 134), cv2.FILLED) # Highlight the button on hover
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

                # Calculate distance between thumb (lmList[4]) and index finger (lmList[8])
                distance = np.sqrt(
                    (lm_list[8][0] - lm_list[4][0])**2 + (lm_list[8][1] - lm_list[4][1])**2)

                # If distance is small, simulate key press
                if distance < 30:
                    # Check for special keys
                    if button.text not in ['ENTER', "BACKSPACE", "SPACE"]:
                        keyboard.press(button.text)  # Press the key
                        # Small delay for better usability & prevent accidental key presses
                        sleep(0.2)
                    else:
                        if button.text == "SPACE":
                            keyboard.press(Key.space)
                            keyboard.release(Key.space)
                            sleep(0.2)

                        elif button.text == "ENTER":
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            sleep(0.2)

                        elif button.text == "BACKSPACE":
                            keyboard.press(Key.backspace)
                            keyboard.release(Key.backspace)
                            sleep(0.2)

                        else:
                            pass
                    cv2.rectangle(img, button.pos, (x + w, y + h),
                                  (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

    # Display the frame with virtual keyboard
    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Exit loop on ESC key press
        break
