# Program to show various ways to
# append data to a file using
# with statement

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open("myfile.txt", "w") as file1:
	# Writing data to a file
	file1.write("Hello \n")
	file1.writelines(L)

# Appending to file
with open("myfile.txt", 'a') as file1:
	file1.write("Today")


# Reading from file
with open("myfile.txt", "r+") as file1:
	# Reading form a file
	print(file1.read())
