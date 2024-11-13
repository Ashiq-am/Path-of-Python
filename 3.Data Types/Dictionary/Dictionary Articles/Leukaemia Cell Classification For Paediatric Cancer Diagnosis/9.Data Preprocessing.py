def read_and_crop_image(image_path):
	# Read image using PIL
	img = Image.open(image_path)
	image = np.array(img) # Convert PIL image to NumPy array

	# Convert Color System from BGR(Blue, Green, Red) to GRAY
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

	# Apply Otsu's Thresholding
	thresh = cv.threshold(
		gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

	# Apply threshold
	result = cv.bitwise_and(image, image, mask=thresh)
	result[thresh == 0] = [255, 255, 255]
	(x, y, z_) = np.where(result > 0)
	mnx = (np.min(x))
	mxx = (np.max(x))
	mny = (np.min(y))
	mxy = (np.max(y))

	# Crop Image
	crop_img = image[mnx:mxx, mny:mxy, :]

	# Resize image
	border_v = 0
	border_h = 0
	if (IMAGE_RESIZE_Y / IMAGE_RESIZE_X) >= (crop_img.shape[0] / crop_img.shape[1]):
		border_v = int((((IMAGE_RESIZE_Y / IMAGE_RESIZE_X) *
						crop_img.shape[1]) - crop_img.shape[0]) / 2)
	else:
		border_h = int((((IMAGE_RESIZE_Y / IMAGE_RESIZE_X) *
						crop_img.shape[0]) - crop_img.shape[1]) / 2)

	crop_img = cv.copyMakeBorder(
		crop_img, border_v, border_v, border_h, border_h, cv.BORDER_CONSTANT, 0)
	resized_image = cv.resize(crop_img, (IMAGE_RESIZE_X, IMAGE_RESIZE_Y))

	# Return colorful image if KEEP_COLOR set
	if KEEP_COLOR:
		return resized_image
	else:
		return cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
