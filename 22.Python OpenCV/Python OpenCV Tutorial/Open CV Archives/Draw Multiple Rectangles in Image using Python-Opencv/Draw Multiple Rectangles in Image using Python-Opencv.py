# importing OpenCV(cv2) module
import cv2

# Read RGB image
img = cv2.imread("D:\Naveen\gfg.PNG")

# Draw rectangles
# Red rectangle
cv2.rectangle(img, (100, 560), (700, 480),
			(0, 0, 255), 3)

# Blue rectangle
cv2.rectangle(img, (650, 450), (420, 240),
			(255, 0, 0), 5)

# Green rectangle
cv2.rectangle(img, (150, 450), (380, 240),
			(0, 255, 0), 4)

# Output img with window name as 'image'
cv2.imshow('image', img)

# Maintain output window utill
# user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()
