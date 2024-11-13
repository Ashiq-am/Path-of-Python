# Python program to find the
# frequency of largest element


L = [1, 2, 8, 5, 8, 7, 8]
d = {}

# find the largest element
largest = max(L)

for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d[largest])
