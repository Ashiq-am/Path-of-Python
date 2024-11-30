d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys we want to keep
keys = ["a", "c"]

# Create a new dictionary with specific keys
new = {key: d[key] for key in keys if key in d}
print(new)