a = [1, 2, 3, 4]
i = 0

while i < len(a):
    if a[i] % 2 == 0:
        a[i] = a[i] * 2
    i += 1

print(a)