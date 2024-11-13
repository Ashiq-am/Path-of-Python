for root, folders, files in list_of_files:
	for file in files:
		file_path = Path(os.path.join(root, file))
		Hash_file = hashlib.md5(open(
		file_path,'rb').read()).hexdigest()
