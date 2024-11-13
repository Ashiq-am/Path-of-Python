# Import module
import os
from pathlib import Path

# Assign directory
directory = r"C:\Users\Lenovo\Downloads\gfg-test"

# Find all files from directory
files = Path(directory).glob("*")
# Iterate over files in directory
for filename in files:
	# Open file
	with open(os.path.join(directory, filename)) as f:
		print(f"Content of '{filename}'")
		# Read content of file
		print(f.read())
	print()
