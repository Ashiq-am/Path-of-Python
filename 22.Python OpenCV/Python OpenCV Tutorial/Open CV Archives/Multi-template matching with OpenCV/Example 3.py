# Passing the image to matchTemplate method
match = cv2.matchTemplate(image=img_gray,
						templ=temp_gray,
						method=cv2.TM_CCOEFF_NORMED)
