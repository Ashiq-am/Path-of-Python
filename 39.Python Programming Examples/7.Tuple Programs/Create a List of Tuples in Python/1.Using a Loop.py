a = [1, 2, 3]
b = ['apple', 'orange', 'cherry']

# Initialize an empty list
res = []

# Using a loop to create tuples and add them to the list
for i in range(len(a)):
    res.append((a[i], b[i]))

print(res)