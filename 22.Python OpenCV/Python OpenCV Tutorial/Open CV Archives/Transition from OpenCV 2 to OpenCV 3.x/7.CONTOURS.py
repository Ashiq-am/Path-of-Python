# OpenCV 2.4
contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# OpenCV 3.4.1
im, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
										cv2.CHAIN_APPROX_NONE)
