a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

# Convert the first list to a set
a_set = set(a)

# Convert the second list to a set
b_set = set(b)

res = a_set == b_set
print(res)