a = [1, 2, 3, 4]

for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = a[i] * 2

print(a)