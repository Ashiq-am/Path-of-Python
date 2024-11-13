import os

# Create a new directory
os.mkdir("example_directory")

# Change the current working directory
os.chdir("example_directory")

# List files in the current directory
files = os.listdir()
print("Files in the current directory:", files)