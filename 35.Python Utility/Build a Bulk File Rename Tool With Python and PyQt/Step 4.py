def renameFiles(self):
	# Get the folder, search pattern, and replacement
	# string from the line edits
	folder = self.folderEdit.text()
	search = self.searchEdit.text()
	replace = self.replaceEdit.text()

	# Check if the folder and search pattern are not empty
	if folder and search:
		# Loop through all the files in the folder
		for filename in os.listdir(folder):
			# Check if the file matches the search pattern
			if search in filename:
				# Get the file path
				filepath = os.path.join(folder, filename)
				# Separate the file name and file extension
				file_name, file_ext = os.path.splitext(filename)
				# Generate the new file name by replacing the
				# search pattern with the replacement string
				new_file_name = file_name.replace(search, replace)
				# Generate the new file name with the file extension
				new_name = new_file_name + file_ext
				# Generate the new file path
				new_path = os.path.join(folder, new_name)
				# Rename the file
				os.rename(filepath, new_path)

	# Show a message box to confirm that the files have been renamed
	QtWidgets.QMessageBox.information(
		self, 'Renamed', 'Files have been renamed')
