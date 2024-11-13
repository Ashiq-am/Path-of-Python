# Import module
import glob
import os

# Assign directory
directory = r"C:\Users\Lenovo\Downloads\gfg-test"

# Iterate over files in directory
for filename in glob.glob(f"{directory}/*"):
	# Open file
	with open(os.path.join(directory, filename)) as f:
		print(f"Content of '{filename}'")
		# Read content of file
		print(f.read())
	print()
