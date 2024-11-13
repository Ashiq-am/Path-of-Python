# Python program to explain shutil.unpack_archive() method

# importing shutil module
import shutil

# Full path of
# the archive file
filename = "/home/User/Downloads/file.zip"

# Target directory
extract_dir = "/home/ihritik/Documnets"

# Format of archie file
archive_format = "zip"

# Unpack the archive file
shutil.unpack_archive(filename, extract_dir, archive_format)
print("Archive file unpacked successfully.")
