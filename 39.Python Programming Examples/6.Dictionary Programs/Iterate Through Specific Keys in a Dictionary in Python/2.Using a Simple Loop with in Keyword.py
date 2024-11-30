d = {"a": 1, "b": 2, "c": 3, "d": 4}

# List of keys we want to iterate over
keys = ["a", "b", "e", "d"]

for key in keys:
  # Check if key exists in the dictionary
    if key in d:
        print(key, d[key])