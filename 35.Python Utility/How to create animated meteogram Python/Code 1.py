# importing path library from pathlib package
from pathlib import Path

# extracting meteograms by specifying
# path of the folder
image_path = Path('../input/meteogram')

# images from folder is stored in image_list
images = list(image_path.glob('*.png'))
image_list = []
for file_name in images:
    # imread() creating numpy array
    # of every image stored in image_list
    image_list.append(imageio.imread(file_name))
