import os
from functools import partial

root_directory = 'Documents/abc'

list = ('one/sub_file_1', 'two/sub_file_2', 'three/sub_file_3')

concat_root_path = partial(os.path.join, root_directory)
make_directory = partial(os.makedirs, exist_ok=True)

for path_items in map(concat_root_path, list):
	make_directory(path_items)
