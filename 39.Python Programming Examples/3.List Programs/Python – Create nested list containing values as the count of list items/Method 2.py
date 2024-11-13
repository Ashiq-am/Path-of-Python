l = [1, 2, 3, 4, 5]

for i in range(len(l)):
    l[i] = [i + 1 for j in range(i + 1)]

print(l)
