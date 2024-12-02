from functools import reduce

# Tuple with Mixed Types
t = (1, 2, 3, 'Learn', 'Python', 'Programming')

# Convert Tuple to String
res = reduce(lambda x, y: str(x) + ' ' + str(y), t)

print(res)