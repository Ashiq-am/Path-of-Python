# Python3 program to Find groups
# of strictly increasing numbers within

def groupSequence(x):
    it = iter(x)
    prev, res = next(it), []

    while prev is not None:
        start = next(it, None)

        if prev + 1 == start:
            res.append(prev)
        elif res:
            yield list(res + [prev])
            res = []
        prev = start


# Driver program
l = [8, 9, 10, 7, 8, 1, 2, 3]
print(list(groupSequence(l)))
