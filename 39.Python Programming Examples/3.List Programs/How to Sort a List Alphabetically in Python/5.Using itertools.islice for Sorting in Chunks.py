from itertools import islice

a = ["John", "Alice", "Eve", "Bob", "Charlie"]

# Split and sort in chunks of 2
it = iter(a)
b = [sorted(list(islice(it, 2))) for _ in range(0, len(a), 2)]

print(b)