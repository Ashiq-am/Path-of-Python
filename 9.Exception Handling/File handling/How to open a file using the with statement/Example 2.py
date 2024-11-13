# appending string to file
with open("geeksforgeeks.txt", "a") as gfg_file:
    gfg_file.write("Hello Geeks!")

# reading the file contents
# to veriy if successfully appended the data
with open("geeksforgeeks.txt", "r") as gfg_file:
    lines = gfg_file.readlines()
    print(lines)
