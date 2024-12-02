f = open("file.txt", "r")

# Move the pointer to the end of the file
f.seek(0, 2)
if f.tell() == 0:
    print("The file is empty")
else:
    print("The file is not empty")
f.close()