import cv2, csv, time

video = cv2.VideoCapture('Location to Video')
source, image = video.read()

# Save the image fot ROI Selection
cv2.imwrite("frame.jpg", image)
video.release()
cv2.destroyAllWindows()
