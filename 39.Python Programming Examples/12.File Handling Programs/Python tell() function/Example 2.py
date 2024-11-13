# Python program to demonstrate
# tell() method

# Opening file
fp = open("sample.txt", "r")
fp.read(8)

# Print the position of handle
print(fp.tell())

# Closing file
fp.close()
