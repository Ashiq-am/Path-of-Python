import os

# File path
a = "myfile.txt"

# Check if the file exists and is a file
if os.path.isfile(a):
    print("File exists and is a file")
else:
    print("File does not exist or is not a file")