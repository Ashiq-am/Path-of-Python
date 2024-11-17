# displaying and saving image
img[top_y:bottom_y, left_x:right_x] = result
cv2.imwrite("watermarked.jpg", img)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
