# Get the dimensions of the images
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

# Get the canvas dimesions
pts = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
dst = cv2.perspectiveTransform(pts, H)
img2_warped = cv2.warpPerspective(img2, H, (w1 + w2, h1))

# Place the first image on the canvas
img2_warped[0:h1, 0:w1] = img1
