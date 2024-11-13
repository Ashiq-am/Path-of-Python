# program to find capacity of the list
import sys
l = []
size = sys.getsizeof(l)
print("size of an empty list :", size)

# append five element in the list
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

# calculate total size of the list after appending five element
print("Now total size of a list :", sys.getsizeof(l))

# calculate capacity of the list after appending five element
c = (sys.getsizeof(l)-size)//8
print("capacity of the list is:", c)
print("length of the list is:", len(l))

# calculate space left the list after appending five element
spaceleft =((sys.getsizeof(l)-size)-len(l)*8)//8
print("space left in the list is:", spaceleft)
