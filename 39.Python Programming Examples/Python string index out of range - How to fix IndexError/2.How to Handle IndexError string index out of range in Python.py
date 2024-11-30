s = "GeeksforGeeks"
index = -14  # Invalid index

# condition for both +ve and -ve index
if -len(s) <= index < len(s):
    print("Character at index:", s[index])
else:
    print("Index out of range!")