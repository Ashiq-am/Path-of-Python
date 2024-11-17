# finding the largest pair of
# eyes in the image
if len(eyes) >= 2:
	eye = eyes[:, 2]
	container1 = []
	for i in range(0, len(eye)):
		container = (eye[i], i)
		container1.append(container)
	df = pd.DataFrame(container1, columns=[
					"length", "idx"]).sort_values(by=['length'])
	eyes = eyes[df.idx.values[0:2]]
