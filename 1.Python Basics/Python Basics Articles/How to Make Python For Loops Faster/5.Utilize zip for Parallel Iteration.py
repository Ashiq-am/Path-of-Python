# Before optimization
for i in range(len(a)):
    process(a[i], b[i])

# After optimization
for i, j in zip(a, b):
    process(i, j)