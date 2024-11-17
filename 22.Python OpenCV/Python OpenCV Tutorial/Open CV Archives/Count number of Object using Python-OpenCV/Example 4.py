canny = cv2.Canny(blur, 30, 150, 3)
plt.imshow(canny, cmap='gray')
