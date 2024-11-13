l = [1, 2, 3, 4, 5]
l = [[i+1 for j in range(l[i])] for i in range(len(l))]
print(l)
