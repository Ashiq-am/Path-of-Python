# importing the zipfile module
from zipfile import ZipFile

# loading the temp.zip and creating a zip object
with ZipFile("C:\\Users\\sai mohan pulamolu\\Desktop\
			\\geeks_dir\\temp\\temp.zip", 'r') as zObject:

	# Extracting specific file in the zip
	# into a specific location.
	zObject.extract(
		"text1.txt", path="C:\\Users\\sai mohan pulamolu\\D\
		esktop\\geeks_dir\\temp")
zObject.close()
