l = ["apple", "banana", "cherry", "date"]

# Strings to check

s = ["banana", "date"]

# Check if all strings exist in the list
if all(item in l for item in s):
    print("All strings are present.")

else:

    print("Some strings are missing.")