from itertools import islice

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3

# Create an iterator
it = iter(a)

# Use islice to generate chunks
chunks = []
for _ in range(0, len(a), n):
    chunks.append(list(islice(it, n)))

print(chunks)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8]]