a = ["apple", "banana", "cherry", "date"]

# Strings to check
s = ["banana", "date"]

# Check using a loop
all_present = True

for item in s:
    if item not in a:
        all_present = False

        break

if all_present:
    print("Found")
else:
    print("Not Found")