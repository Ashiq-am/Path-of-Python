# importing the shutil module
import shutil

# storing the current path of file.txt
# in the source variable
source = 'D:/projects/base/subfolder/file.txt'

# storing the destination path in the
# destination variable
destination = 'D:/projects/base/file.txt'

# calling the shutil.copyfile() method
shutil.copyfile(source,destination)
