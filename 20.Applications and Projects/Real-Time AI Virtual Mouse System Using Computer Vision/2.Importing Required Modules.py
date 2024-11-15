# To create GUI
import tkinter as tk
from PIL import ImageTk, Image
pyautogui.FAILSAFE = False
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
# Gesture Encodings
class Gest(IntEnum):
	# Binary Encoded
	FIST = 0
	PINKY = 1
	RING = 2
	MID = 4
	LAST3 = 7
	INDEX = 8
	FIRST2 = 12
	LAST4 = 15
	THUMB = 16
	PALM = 31
	# Extra Mappings
	V_GEST = 33
	TWO_FINGER_CLOSED = 34
	PINCH_MAJOR = 35
	PINCH_MINOR = 36

# Multi-handedness Labels
class HLabel(IntEnum):
	MINOR = 0
	MAJOR = 1
