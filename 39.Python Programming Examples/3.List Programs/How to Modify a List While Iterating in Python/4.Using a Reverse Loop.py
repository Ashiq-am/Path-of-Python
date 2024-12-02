a = [1, 2, 3, 4]

for item  in a.copy():
    if item % 2 != 0:
        a.remove(item)

print(a)