# import required module
from pathlib import Path

# get the path/directory
folder_dir = 'Gfg images'

# iterate over files in
# that directory
images = Path(folder_dir).glob('*.png')
for image in images:
	print(image)
