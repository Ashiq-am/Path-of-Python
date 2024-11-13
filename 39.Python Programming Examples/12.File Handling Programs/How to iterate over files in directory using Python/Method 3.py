# import required module
from pathlib import Path

# assign directory
directory = 'files'

# itrate over files in
# that directory
files = Path(directory).glob('*')
for file in files:
	print(file)
