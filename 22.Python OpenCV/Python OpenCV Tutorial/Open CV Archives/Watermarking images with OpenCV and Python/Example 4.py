# adding watermark to the image
destination = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(destination,1, logo, 0.5, 0)
