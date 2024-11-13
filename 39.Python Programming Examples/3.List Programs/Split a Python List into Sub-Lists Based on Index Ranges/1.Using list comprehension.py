Input = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# The index ranges to split at
indices = [(1, 4), (3, 7)]

print([Input[a:b+1] for (a, b) in indices])
