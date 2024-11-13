def print_file_path():
	try:
		print(__file__)
	except NameError:
		print("File path not available.")

print_file_path()
