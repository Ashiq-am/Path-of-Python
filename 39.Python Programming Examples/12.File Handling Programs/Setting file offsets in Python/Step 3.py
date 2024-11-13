# open the file
fhand = open("emails.txt", "r")

# check default value of offset
print(f"The default position of offset is: {fhand.tell()}")
