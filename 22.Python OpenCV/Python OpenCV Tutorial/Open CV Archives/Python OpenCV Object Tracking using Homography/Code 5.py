# initializing height and width of the image
h, w = img.shape

# saving all points in pts
pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)

# applying perspective algorithm
dst = cv2.perspectiveTransform(pts, matrix)
