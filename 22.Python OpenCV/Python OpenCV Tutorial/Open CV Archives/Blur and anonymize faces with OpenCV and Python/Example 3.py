# convert the frame into grayscale(shades of black & white)
gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
face = cascade.detectMultiScale(gray_image,
								scaleFactor=2.0,
								minNeighbors=4)
