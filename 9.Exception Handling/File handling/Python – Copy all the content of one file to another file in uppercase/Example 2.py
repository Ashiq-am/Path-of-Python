# To open the first file in read mode
f1 = open("sample file 1.txt", "r")

# To open the second file in append mode
f2 = open("sample file 2.txt", "a")

# For loop to traverse through the file
for line in f1:
    # Writing the content of the first
    # file to the second file

    # Using upper() function
    # to capitalize the letters
    f2.write(line.upper())
