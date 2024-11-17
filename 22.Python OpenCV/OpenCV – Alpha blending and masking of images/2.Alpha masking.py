import cv2
im = cv2.imread("spectacles.png", cv2.IMREAD_UNCHANGED)
_, mask = cv2.threshold(im[:, :, 3], 0, 255, cv2.THRESH_BINARY)
cv2.imwrite('mask.jpg', mask)
