# REMOVE 20 PIXELS FROM EACH SIDE
imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))

# APPLY ADAPTIVE THRESHOLD
imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre, 3)

# Image Array for Display
imageArray = ([img, imgGray, imgThreshold, imgContours],
              [imgBigContour, imgWarpColored, imgWarpGray, imgAdaptiveThre])

# WRITE IMAGE
cv2.imwrite("Scanned/myImage" + str(count) + ".jpg", imgWarpColored)
count += 1

else:
imageArray = ([img, imgGray, imgThreshold, imgContours],
              [imgBlank, imgBlank, imgBlank, imgBlank])

# LABELS FOR DISPLAY
labels = [["Original", "Gray", "Threshold", "Contours"],
          ["Biggest Contour", "Warp Perspective", "Warp Gray", "Adaptive Threshold"]]

stackedImage = utlis.stackImages(imageArray, 0.75, labels)
cv2.imshow("Result", stackedImage)

if cv2.waitKey(1) & 0xFF == ord('q'):
    break
