d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys to filter
keys = ["a", "c", "d"]

# Use filter to get keys that are in d
new_keys = filter(lambda k: k in d, keys)

# Iterate through filtered keys
for key in new_keys:
    print(key, d[key])