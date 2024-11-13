# Python code to implement startswith()
# and endswith() function.

str = "GeeksforGeeks"

# startswith()
print(str.startswith("Geeks"))
print(str.startswith("Geeks", 4, 10))
print(str.startswith("Geeks", 8, 14))

print("\n")

# endswith
print(str.endswith("Geeks"))
print(str.endswith("Geeks", 2, 8))
print(str.endswith("for", 5, 8))
