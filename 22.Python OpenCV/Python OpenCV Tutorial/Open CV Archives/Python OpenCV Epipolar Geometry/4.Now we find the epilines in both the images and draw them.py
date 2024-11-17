# Find epilines corresponding to points
# in right image (second image) and
# drawing its lines on left image
linesLeft = cv2.computeCorrespondEpilines(ptsRight.reshape(-1,
														1,
														2),
										2, F)
linesLeft = linesLeft.reshape(-1, 3)
img5, img6 = drawlines(imgLeft, imgRight,
					linesLeft, ptsLeft,
					ptsRight)

# Find epilines corresponding to
# points in left image (first image) and
# drawing its lines on right image
linesRight = cv2.computeCorrespondEpilines(ptsLeft.reshape(-1, 1, 2),
										1, F)
linesRight = linesRight.reshape(-1, 3)

img3, img4 = drawlines(imgRight, imgLeft,
					linesRight, ptsRight,
					ptsLeft)

plt.subplot(121), plt.imshow(img5)
plt.subplot(122), plt.imshow(img3)
plt.show()
