# Sorting a list ignoring case sensitivity
a = ["john", "Alice", "eve", "BOB"]

# Sorting alphabetically while ignoring case
b = sorted(a, key=str.lower)

print(b)


# Sorting a list based on string length
a = ["apple", "kiwi", "banana", "pear"]

# Sorting the list by length
a.sort(key=len)

print(a)