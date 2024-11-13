import pathlib

# function to return the file extension
file_extension = pathlib.Path('my_file.txt').suffix
print("File Extension: ", file_extension)
