list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

result = [(index+1) * value for index, value in enumerate(zip(list_a, list_b))]
print(result)
