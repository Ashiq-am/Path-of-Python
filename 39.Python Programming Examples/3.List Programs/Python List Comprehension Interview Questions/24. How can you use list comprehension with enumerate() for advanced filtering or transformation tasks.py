a = [1, 2, 3, 4, 5, 6]
result = [value**2 for index, value in enumerate(a) if index % 2 == 0 and value % 2 != 0]
print(result)