# Python program to demonstrate
# tell() method

# for reading binary file we
# have to use "wb" in file mode.
fp = open("sample2.txt", "wb")
print(fp.tell())

# Writing to file
fp.write(b'1010101')

print(fp.tell())

# Closing file
fp.close()
