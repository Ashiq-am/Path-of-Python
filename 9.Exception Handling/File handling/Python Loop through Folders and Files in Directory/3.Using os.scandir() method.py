# Import module
import os

# Assign directory
directory = r"C:\Users\Lenovo\Downloads\gfg-test"

# Iterate over files in directory
for filename in os.scandir(directory):
	# Open file
	with open(os.path.join(directory, filename)) as f:
		print(f"Content of '{filename}'")
		# Read content of file
		print(f.read())
	print()
