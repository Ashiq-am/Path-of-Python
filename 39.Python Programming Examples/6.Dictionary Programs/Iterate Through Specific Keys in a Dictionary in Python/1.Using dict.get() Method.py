d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys we want to check
keys = ["a", "b", "e", "d"]

# Iterate through specific keys using get()
for key in keys:
   # Returns None if key doesn't exist
    value = d.get(key)
    if value is not None:
        print(key, value)
