a = {
    1: [1, 2],
    2: [3, 4, 6]
}

result = {key: [i for i, val in enumerate(x)] for key, x in a.items()}

print(result)