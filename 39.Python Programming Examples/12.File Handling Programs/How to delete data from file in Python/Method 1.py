# code to delete entire data along with file
import os

# check if file exists
if os.path.exists("sample.txt"):
	os.remove("sample.txt")

	# Print the statement once
	# the file is deleted
	print("File deleted !")

else:

	# Print if file is not present
	print("File doesnot exist !")
