# Copying the original image
from email.mime import image

import cv2

output = image.copy()

# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (500, 550),cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
