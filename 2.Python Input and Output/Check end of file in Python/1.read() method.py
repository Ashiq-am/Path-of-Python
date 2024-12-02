f = open("file.txt", "r")

# Read the entire content of the file into the variable 'content'
content = f.read()
# Check if the file content is empty
if content == "":
    print("End of file reached")
f.close()