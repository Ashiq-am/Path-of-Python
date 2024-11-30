# Splitting a list based on a condition
li = [1, 2, 3, 4, 5, 6, 7, 8]
a = []
b = []

for i in li:

    # Keeping the even numbers in list a after splitting
    if i % 2 == 0:
        a.append(i)

    # Keeping the odd numbers in list b after splitting
    else:
        b.append(i)

print(a, b)