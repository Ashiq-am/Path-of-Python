import os
import glob

# Path to the directory where
# the files reside
path = r"C:\Users\applese\images"

# Getting the list of files/directories
# in the specified path Filtering the
# list to exclude the directory names
files = list(filter(os.path.isfile, glob.glob(path + "\*")))

# Sorting file list based on the
# creation time of the files
files.sort(key=os.path.getctime)

# Displaying the sorted list
print(files)
