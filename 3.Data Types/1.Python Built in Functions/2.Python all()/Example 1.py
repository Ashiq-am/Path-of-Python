# All elements of list are true
l = [4, 5, 1]
print(all(l))

# All elements of list are false
l = [0, 0, False]
print(all(l))

# Some elements of list are
# true while others are false
l = [1, 0, 6, 7, False]
print(all(l))

# Empty List
l = []
print(all(l))
