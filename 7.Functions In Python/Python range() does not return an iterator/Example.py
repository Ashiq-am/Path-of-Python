# Python program to understand range

# creates a demo range
demo = range(1, 31, 2)

# print the range
print(demo)

# print the start of range
print(demo.start)

# print step of range
print(demo.step)

# print the index of element 23
print(demo.index(23))

# since 30 is not present it will give error
print(demo.index(30))
