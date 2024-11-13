# Python program for reading
# from file


h = open('GFG.txt', 'r')

# Reading from the file
content = h.readlines()

# Varaible for storing the sum
a = 0

# Iterating through the content
# Of the file
for line in content:

    for i in line:

        # Checking for the digit in
        # the string
        if i.isdigit() == True:
            a += int(i)

print("The sum is:", a)
