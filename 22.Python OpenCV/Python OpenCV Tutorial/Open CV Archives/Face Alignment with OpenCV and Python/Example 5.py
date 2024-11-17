# calculating the angle between a, b, c
cv2.circle(img, point_3rd, 2, (255, 0, 0), 2)
a = trignometry_for_distance(left_eye_center, point_3rd)
b = trignometry_for_distance(right_eye_center, point_3rd)
c = trignometry_for_distance(right_eye_center, left_eye_center)
cos_a = (b*b + c*c - a*a)/(2*b*c)
angle = (np.arccos(cos_a) * 180) / math.pi
