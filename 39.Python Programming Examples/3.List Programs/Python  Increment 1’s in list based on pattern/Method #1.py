# Python3 program to increment 1's in
# list based on pattern

def transform(lst):
    previous = 0
    grp = 0
    for elem in lst:
        if elem and not previous:
            grp += 1
        previous = elem
        yield (grp if elem else 0)


# Driver code
lst = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
x = (transform(lst))
res = []
for i in range(0, len(lst)):
    res.append(next(x))
print(res)
