# Example using a dictionary of lists

all_lists = list(map(lambda i: [i * j for j in range(3)], range(5)))
print(all_lists)
