# function to check whether the file is closed
def checkFileClosed(file_obj):
	# check if file is closed using `closed` property
	if file_obj.closed == True:
		print("Your file is closed.")
	else:
		print("Your file is open.")


# Opening the `data.csv` file in read mode
file_obj = open("data.csv", "r")

# check if file is closed
checkFileClosed(file_obj)

print("Now closing 'data.csv' file.")
# close the file
file_obj.close()

# again check if file is closed
checkFileClosed(file_obj)
