a = [10, 20, 30, 40, 50]

# `i` is the index, `val` is the value at that index
res = [i for i, val in enumerate(a) if val == 30]

print("Indices of 30:", res)