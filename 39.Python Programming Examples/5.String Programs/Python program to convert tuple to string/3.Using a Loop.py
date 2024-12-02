t = (1, 2, 3, 'Learn', 'Python', 'Programming')

# Convert Tuple to String
res = ''

# Iterates over each element of tuple
for val in t:
    # First convert each item to string then append
    # to res with a trailing space
    res += str(val) + ' '

# Removes extra space from both end of res.
res = res.strip()

print(res)