# importing the zipfile module
from zipfile import ZipFile

# loading the temp.zip and creating a zip object
with ZipFile("C:\\Users\\sai mohan pulamolu\\\
			Desktop\\geeks_dir\\temp\\temp.zip", 'r') as zObject:

	# Extracting all the members of the zip
	# into a specific location.
	zObject.extractall(
		path="C:\\Users\\sai mohan pulamolu\\Desktop\\geeks_dir\\temp")
