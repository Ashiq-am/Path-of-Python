import os

file_path = "myfile.txt"
if os.access(file_path, os.F_OK):
    print("File exists")
else:
    print("File does not exist")