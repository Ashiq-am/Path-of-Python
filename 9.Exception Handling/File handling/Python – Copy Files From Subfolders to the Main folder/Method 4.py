# importing shutil module
import shutil

# Source file
source = 'D:/projects/base/subfolder/file.txt'

# Open the source file
# in read mode and
# get the file object
fsrc = open(source, 'r')

# destination file
dest = 'D:/projects/base/file.txt'

# Open the destination file
# in write mode and
# get the file object
fdst = open(dest, 'w')

# Now, copy the contents of
# file object f1 to f2
# using shutil.copyfileobj() method
shutil.copyfileobj(fsrc, fdst)

# We can also specify
# the buffer size by paasing
# optional length parameter
# like shutil.copyfileobj(fsrc, fdst, 1024)


# Close file objects
fdst.close()
fsrc.close()
