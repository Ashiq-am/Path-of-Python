# Input array of boolean elements
b = np.array([True, True, False, True, False])

# Printing input list
print(list(b))

# Converting using bitwise_not function
b = np.bitwise_not(b)

# Printing output list
print(list(b))
