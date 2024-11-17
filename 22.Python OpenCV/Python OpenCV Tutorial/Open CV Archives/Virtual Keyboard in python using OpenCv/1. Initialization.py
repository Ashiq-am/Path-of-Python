import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
from pynput.keyboard import Controller, Key

# Initialize video capture
cap = cv2.VideoCapture(0)
# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)  # Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 520)   # Height

cv2.namedWindow("Virtual Keyboard", cv2.WINDOW_NORMAL)

# Initialize HandDetector for hand tracking
# Detection and tracking confidence thresholds from CVZone
detector = HandDetector(detectionCon=0.8, minTrackCon=0.2)

# Define virtual keyboard layout
keyboard_keys = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["SPACE", "ENTER", "BACKSPACE"]
]

keyboard = Controller()  # Create a keyboard controller instance
