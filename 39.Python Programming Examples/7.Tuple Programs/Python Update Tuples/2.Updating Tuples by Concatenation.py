# Original tuple
tup1 = (1, 2, 3, 4)

# Concatenate new values to form a new tuple
tup2 = (10,) + tup1[1:]  # Keep the rest of the tuple intact

# Printing the updated tuple
print(tup2)