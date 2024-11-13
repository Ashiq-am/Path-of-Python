# Python program to demonstrate
# shutil.rmtree()

import shutil
import os

# location
location = "D:/Pycharm projects/GeeksforGeeks/"

# directory
dir = "Authors"

# path
path = os.path.join(location, dir)

# removing directory
shutil.rmtree(path, ignore_errors = False)

# making ignore_errors = True will not raise
# a FileNotFoundError
