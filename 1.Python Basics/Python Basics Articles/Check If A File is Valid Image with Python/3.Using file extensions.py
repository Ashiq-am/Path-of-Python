import os

# Directory path
directory_path = r"C:\Users\shrav\Desktop\GFG"

# File names
file_names = ["GFG.txt", "GFG.jpg"]

# Get full file paths
file_paths = [os.path.join(directory_path, file_name)
			for file_name in file_names]

# 4. Using file extension
def is_valid_image_extension(file_name):
	valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
	return any(file_name.lower().endswith(ext) for ext in valid_extensions)

# Example
for file_name in file_names:
	print(f"File: {file_name}")
	if os.path.exists(file_name): # Check if the file exists
		print("Using file extension:", is_valid_image_extension(file_name))
		print()
	else:
		print(f"File '{file_name}' not found.")
		print()
