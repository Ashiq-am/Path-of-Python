# program to find capacity of the list

import sys
l = []
size = sys.getsizeof(l)
print("size of an empty list :", size)

# append an element in the list
l.append(1)

# calculate total size of the list after appending one element
print("Now total size of a list :", sys.getsizeof(l))

# calculate capacity of the list after appending one element
# Considering block size as 8.
capacity = (sys.getsizeof(l)-size)//8
print("capacity of the list is:", capacity)
print("length of the list is :", len(l))

# calculate space left the list after appending one element
spaceleft = ((sys.getsizeof(l)-size)-len(l)*8)//8
print("space left in the list is:", spaceleft)
