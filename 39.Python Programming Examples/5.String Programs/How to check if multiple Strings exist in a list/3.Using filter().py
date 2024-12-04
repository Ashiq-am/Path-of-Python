a = ["apple", "banana", "cherry", "date"]

# Strings to check
s = ["banana", "date"]

# Check if all strings match
matching = list(filter(lambda x: x in a, s))

if len(matching) == len(s):
    print("Found")
else:
    print("Not Found")