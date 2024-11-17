# blur the face which is in the rectangle
image[y:y+h, x:x+w] = cv2.medianBlur(image[y:y+h, x:x+w], 35)
