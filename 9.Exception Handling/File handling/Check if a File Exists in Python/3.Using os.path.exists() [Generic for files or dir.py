import os

# File path
a = "myfile.txt"

# Check if the file exists
if os.path.exists(a):
    print("File exists")
else:
    print("File does not exist")