# import module
import os

# assing size
size = 0

# assign folder path
Folderpath = 'C:/Users/Geetansh Sahni/Documents/R'

# get size
for ele in os.scandir(Folderpath):
    size += os.stat(ele).st_size

print(size)
