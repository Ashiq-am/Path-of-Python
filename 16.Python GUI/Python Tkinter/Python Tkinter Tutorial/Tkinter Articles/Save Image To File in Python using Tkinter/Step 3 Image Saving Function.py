def save_image(file_path):
	save_dir = "saved_images"
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)
	filename = os.path.basename(file_path)
	shutil.copy(file_path, os.path.join(save_dir, filename))
	print("Image saved to:", os.path.join(save_dir, filename))
