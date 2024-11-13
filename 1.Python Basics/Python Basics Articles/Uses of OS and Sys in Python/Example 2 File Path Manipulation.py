import os

# Join paths to create a file path
file_path = os.path.join("path", "to", "file.txt")

# Get the absolute path of a file
absolute_path = os.path.abspath("file.txt")
print("Absolute path:", absolute_path)