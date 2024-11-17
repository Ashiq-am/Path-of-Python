def seam_carve(img, new_width, new_height):
	for i in range(img.shape[1] - new_width):
		energy_map = np.abs(cv2.Scharr(img, -1, 1, 0)) \
			+ np.abs(cv2.Scharr(img, -1, 0, 1))
		energy_map = energy_map.astype(np.float64)
		min_energy_map = np.zeros_like(energy_map)
		min_energy_map[0] = energy_map[0]
		for row in range(1, img.shape[0]):
			for col in range(img.shape[1]):
				if col == 0:
					min_energy_map[row, col] = energy_map[row, col] \
						+ min(min_energy_map[row - 1, col],
							min_energy_map[row - 1, col + 1])
				elif col == img.shape[1] - 1:
					min_energy_map[row, col] = energy_map[row, col] \
						+ min(min_energy_map[row - 1, col - 1],
							min_energy_map[row - 1, col])
				else:
					min_energy_map[row, col] = energy_map[row, col] \
						+ min(min_energy_map[row - 1, col - 1],
							min_energy_map[row - 1, col],
							min_energy_map[row - 1, col + 1])
		seam_mask = np.ones_like(img[:, :, 0])
		col = np.argmin(min_energy_map[-1])
		for row in reversed(range(img.shape[0])):
			seam_mask[row, col] = 0
			if col == 0:
				col = np.argmin(min_energy_map[row - 1, col:col + 2])
			elif col == img.shape[1] - 1:
				col = np.argmin(min_energy_map[row - 1, col - 1:col + 1]) \
					+ col - 1
			else:
				col = np.argmin(min_energy_map[row - 1, col - 1:col + 2]) \
					+ col - 1
		img = cv2.resize(img, (new_width, new_height))
		seam_mask = cv2.resize(seam_mask, (new_width, new_height))
		for channel in range(img.shape[2]):
			img[:, :, channel] = np.multiply(img[:, :, channel], seam_mask)
		img = img.astype(np.uint8)


	return img
