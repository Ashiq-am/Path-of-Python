import os
from PIL import Image

# Directory path
directory_path = r"C:\Users\shrav\Desktop\GFG"

# File names
file_names = ["GFG.txt", "GFG.jpg"]

# Get full file paths
file_paths = [os.path.join(directory_path, file_name)
			for file_name in file_names]

# 1. Using Pillow (PIL)
def is_valid_image_pillow(file_name):
	try:
		with Image.open(file_name) as img:
			img.verify()
			return True
	except (IOError, SyntaxError):
		return False

# Example usage
for file_name in file_names:
	print(f"File: {file_name}")
	if os.path.exists(file_name): # Check if the file exists
		print("Using Pillow (PIL):", is_valid_image_pillow(file_name))
		print()
	else:
		print(f"File '{file_name}' not found.")
		print()
