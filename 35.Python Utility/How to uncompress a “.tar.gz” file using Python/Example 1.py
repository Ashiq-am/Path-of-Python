# importing the "tarfile" module
import tarfile

# open file
file = tarfile.open('gfg.tar.gz')

# extracting file
file.extractall('./Destination_FolderName')

file.close()
