# declaring HandDetector with
# some basic requirements
detector = HandDetector(maxHands=1,
						detectionCon=0.8)

# it detect only one hand from
# video with 0.8 detection confidence
video = cv2.VideoCapture(0)
