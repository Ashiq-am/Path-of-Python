# declaring a list
lst = [1, "Mallika", 2, "Yash"]

# output
output = []

# looping over list
for i in range(0, len(lst)):
    for j in range(0, len(lst)):

        # checking if i and j indexes are not on same element
        if (i != j):
            # add to output
            output.append((lst[i], lst[j]))

# view output
print(output)
