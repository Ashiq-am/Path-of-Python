# Original tuple
tup1 = (1, 2, 3, 4)

# Replace the second and third elements
tup2 = tuple([10] + list(tup1[2:]))

# Printing the updated tuple
print(tup2)