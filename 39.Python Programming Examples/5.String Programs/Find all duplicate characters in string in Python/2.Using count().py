s = "GeeksforGeeks"
res = []

# Iterate over the unique elements in 's'
for c in set(s):  # Use set to avoid repeated checks
    if s.count(c) > 1:
        res.append(c)

print(res)