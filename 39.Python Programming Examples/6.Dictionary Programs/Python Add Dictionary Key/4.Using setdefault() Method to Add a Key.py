d = {1: 10, 2: 20, 3: 30}
d.setdefault(4, 40)  # Adds key 4 with value 40 if it doesn't exist
print(d)

# If the key exists, it will not be added again
d.setdefault(4, 45)  # Doesn't update key 4
print(d)