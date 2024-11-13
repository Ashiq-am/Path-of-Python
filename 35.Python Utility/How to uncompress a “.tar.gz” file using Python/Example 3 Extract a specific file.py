# importing the "tarfile" module
import tarfile

# open file
file = tarfile.open('gfg.tar.gz')

# extracting a specific file
file.extract('sample.txt', './Destination_FolderName')

file.close()
