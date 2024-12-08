a = [(1, 2), (3, 4), (5, 6)]
flattened = [item for sublist in a for item in sublist]
print(flattened)