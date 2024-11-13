def import_file():
	file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
	if file_path:
		# Process the selected file (you can replace this with your own logic)
		print("Selected file:", file_path)
