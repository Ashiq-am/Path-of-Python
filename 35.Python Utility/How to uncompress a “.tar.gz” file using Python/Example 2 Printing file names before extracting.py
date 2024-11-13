# importing the "tarfile" module
import tarfile

# open file
file = tarfile.open('gfg.tar.gz')

# print file names
print(file.getnames())

# extract files
file.extractall('./Destination_FolderName')

# close file
file.close()
