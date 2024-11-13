# importing the shutil module
import shutil

# storing the current file path of file.txt
# in the source variable
source = 'D:/projects/base/subfolder/file.txt'

# storing the destination directory in the
# destination variable
destination = 'D:/projects/base'

# calling the shutil.copy() method
shutil.copy(source,destination)
