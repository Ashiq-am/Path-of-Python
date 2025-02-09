from sortedcontainers import SortedDict

# Creating a dictionary
d = SortedDict({2:"GfG", 1:"Geeks", 3:"POTD"})
print(d)

# Insertion in dictionary
d[-1] = "Hello"
d[0] = "World"
print("After Insertion:", d)

# Deletion in dictionary
del d[-1]
d.pop(3)
print("After Deletion:", d)
