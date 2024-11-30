# Splitting a list into equal-sized chunks
li = [1, 2, 3, 4, 5, 6, 7, 8]

# Number of Chunks
n = 3

# Splitting Chunks and Storing them in List a
a = [li[i:i + n] for i in range(0, len(li), n)]

print(a)