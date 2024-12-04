a = {
    1: [1, 2],
    2: [3, 4, 6]
}

# Using list comprehension to get the indices of all values
result = [[i for i, val in enumerate(x)] for x in a.values()]
print(result)