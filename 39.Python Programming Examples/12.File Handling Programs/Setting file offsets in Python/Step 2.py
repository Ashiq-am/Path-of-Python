# opening the file with reading permissions
fhand = open("emails.txt", "r")

# print the content of the whole file
print(fhand.read())

# close the file
fhand.close()
