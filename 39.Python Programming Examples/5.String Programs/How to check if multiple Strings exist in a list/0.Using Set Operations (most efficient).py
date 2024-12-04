a = ["apple", "banana", "cherry", "date"]

# Strings to check
s = {"banana", "date"}

# Check if all strings exist in the list
if s.issubset(a):
    print("Found")
else:
    print("Not Found")
