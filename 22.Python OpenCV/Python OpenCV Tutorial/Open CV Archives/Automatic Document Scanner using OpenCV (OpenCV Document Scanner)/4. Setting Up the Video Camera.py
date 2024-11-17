webCamFeed = False
url = 'http://192.168.1.6:8080/video'
cap = cv2.VideoCapture(url)
cap.set(10, 160)
heightImg = 640
widthImg = 480
