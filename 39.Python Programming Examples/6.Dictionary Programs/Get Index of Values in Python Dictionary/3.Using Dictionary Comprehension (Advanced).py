a = {
    1: [1, 2],
    2: [3, 4, 6]
}
result = []

# Loop over each list in the dictionary
for x in a.values():
    indices = []
    for i in range(len(x)):
        indices.append(i)
    result.append(indices)

print(result)