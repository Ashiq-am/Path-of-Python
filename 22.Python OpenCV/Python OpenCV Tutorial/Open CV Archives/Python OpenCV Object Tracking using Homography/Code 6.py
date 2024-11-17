# using drawing function for the frame
homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)

# showing the final output
# with homography
cv2.imshow("Homography", homography)
