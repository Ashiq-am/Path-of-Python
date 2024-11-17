# center of right eye
right_eye_center = (
	int(right_eye[0] + (right_eye[2]/2)),
int(right_eye[1] + (right_eye[3]/2)))
right_eye_x = right_eye_center[0]
right_eye_y = right_eye_center[1]
cv2.circle(img, right_eye_center, 2, (255, 0, 0), 3)

# center of left eye
left_eye_center = (
	int(left_eye[0] + (left_eye[2] / 2)),
int(left_eye[1] + (left_eye[3] / 2)))
left_eye_x = left_eye_center[0]
left_eye_y = left_eye_center[1]
cv2.circle(img, left_eye_center, 2, (255, 0, 0), 3)

# finding rotation direction
if left_eye_y > right_eye_y:
	print("Rotate image to clock direction")
	point_3rd = (right_eye_x, left_eye_y)
	direction = -1 # rotate image direction to clock
else:
	print("Rotate to inverse clock direction")
	point_3rd = (left_eye_x, right_eye_y)
	direction = 1 # rotate inverse direction of clock
