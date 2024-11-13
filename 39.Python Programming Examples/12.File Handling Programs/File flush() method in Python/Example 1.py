# openinng the file in read mode
fileObject = open("gfg.txt", "r")

# clearing the input buffer
fileObject.flush()

# reading the content of the file
fileContent = fileObject.read()

# displaying the content of the file
print(fileContent)

# closing the file
fileObject.close()
