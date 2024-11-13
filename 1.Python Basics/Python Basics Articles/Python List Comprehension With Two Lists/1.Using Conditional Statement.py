list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

result = [a + b for a, b in zip(list_a, list_b) if (a + b) % 2 == 0]
print(result)
