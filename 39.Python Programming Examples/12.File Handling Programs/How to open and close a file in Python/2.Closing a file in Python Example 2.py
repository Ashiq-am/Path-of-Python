# open the file using open() function
file = open("sample.txt")

# Reading from file
print(file.read())

# closing the file
file.close()

# Attempt to write in the file
file.write(" Attempt to write on a closed file !")
