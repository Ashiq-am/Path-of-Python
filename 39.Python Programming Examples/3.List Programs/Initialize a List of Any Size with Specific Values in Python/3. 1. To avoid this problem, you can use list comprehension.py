# Initialize a list of 3 distinct empty lists
a = [[] for _ in range(3)]

a[0].append(1)
print(a)

# Output: [[1], [], []]