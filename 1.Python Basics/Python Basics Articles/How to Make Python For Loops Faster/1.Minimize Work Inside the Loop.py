# Before optimization
for i in range(len(a)):
    res = func(a[i])
    print(res)

# After optimization
# Reference the function outside the loop to avoid repeated lookups
b = func
for i in a:
    res = func(i)
    print(res)