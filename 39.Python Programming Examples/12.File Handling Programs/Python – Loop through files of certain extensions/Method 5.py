# importing the module
from pathlib import Path

# directory name
dirname = 'D:\\AllData'

# giving directory name to Path() function
paths = Path(dirname).glob('**/*.exe',)

# iterating over all files
for path in paths:
	print(path) # printing file name
