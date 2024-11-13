import cv2

# Trying to capture images from a non-existing directory
cap = cv2.VideoCapture('non_existing_directory/image_%d.png')

if not cap.isOpened():
    print("Error: CAP_IMAGES: Can't Find Starting Number")
