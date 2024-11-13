import glob

# search .py files
# in the current working directory
for py in glob.glob("*.py"):
	print(py)
