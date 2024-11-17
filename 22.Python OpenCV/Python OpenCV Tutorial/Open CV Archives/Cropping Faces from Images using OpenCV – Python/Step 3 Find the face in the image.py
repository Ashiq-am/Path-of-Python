for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h),
                  (0, 0, 255), 2)

    faces = img[y:y + h, x:x + w]
    cv2.imshow("face", faces)
    cv2.imwrite('face.jpg', faces)

cv2.imshow('img', img)
cv2.waitKey()
