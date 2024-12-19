a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

# Use the sorted() to create
# sorted copies of the lists

# Sorts the first list
a_sorted = sorted(a)

# Sorts the second list
b_sorted = sorted(b)

res = a_sorted == b_sorted
print(res)