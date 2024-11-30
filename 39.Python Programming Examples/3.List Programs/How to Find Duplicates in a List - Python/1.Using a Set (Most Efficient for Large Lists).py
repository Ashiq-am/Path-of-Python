a = [1, 2, 3, 4, 5, 2, 6, 3]

# A set to keep track of elements that have been seen
seen = set()
# A list to store duplicates found in the input list
duplicates = []

# Iterate over each element in the list
for i in a:
    if i in seen:
        duplicates.append(i)
    else:
        seen.add(i)

print(duplicates)