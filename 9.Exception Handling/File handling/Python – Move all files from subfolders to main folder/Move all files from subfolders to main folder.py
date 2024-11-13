import shutil
import os

# Define the source and destination path
source = "Desktop/content/waste/"
destination = "Desktop/content/"

# code to move the files from sub-folder to main folder.
files = os.listdir(source)
for file in files:
	file_name = os.path.join(source, file)
	shutil.move(file_name, destination)
print("Files Moved")
