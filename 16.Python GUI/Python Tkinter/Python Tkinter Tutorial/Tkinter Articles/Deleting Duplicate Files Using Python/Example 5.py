unique_files = dict()
if Hash_file not in unique_files:
	unique_files[Hash_file] = file_path
else:
	os.remove(file_path)
	print(f"{file_path} has been deleted")
