def draw_buttons(img, button_list):
    """
    Draws buttons on the given image.

    Args:
        img (numpy.ndarray): The image on which the buttons will be drawn.
        button_list (list): A list of Button objects representing the buttons to be drawn.

    Returns:
        numpy.ndarray: The image with the buttons drawn.
    """
    for button in button_list:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 20, rt=0)
        cv2.rectangle(img, button.pos, (int(x + w), int(y + h)),
                      (37, 238, 250), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
    return img
