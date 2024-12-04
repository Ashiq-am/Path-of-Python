y = [10, 20, 30, 40, 50]

# Extracts elements at even indices
h = [val for idx, val in enumerate(y) if idx % 2 == 0]
print(h)