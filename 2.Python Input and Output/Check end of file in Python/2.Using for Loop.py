f = open("file.txt", "r")

# Iterate through each line in the file
for line in f:
    print(line, end="")
print("End of file reached")
f.close()