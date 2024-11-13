# Python program to explain shutil.unpack_archive() method

# importing shutil module
import shutil

# Full path of
# the archive file
filename = "/home/User/Downloads/file.zip"

# Unpack the archived file
shutil.unpack_archive(filename)
print("Archive file unpacked successfully.")

# As extract_dir and format parameters
# are not provided So,
# shutil.unpack_archive() method will
# unpack the archive file in
# current working directory and extension
# of the archive filename i.e zip
# will be taken as format to unpack

