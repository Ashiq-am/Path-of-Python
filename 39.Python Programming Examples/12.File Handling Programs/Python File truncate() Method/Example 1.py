# Python program to demonstrate
# truncate() method

fp = open('file1.txt', 'w')

# Truncates the file to specified
# size
fp.truncate(100)

# Closing files
fp.close()
