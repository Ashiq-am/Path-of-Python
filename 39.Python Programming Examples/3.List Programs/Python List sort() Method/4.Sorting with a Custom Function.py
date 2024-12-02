a = [(1, 3), (2, 2), (3, 1)]


def fun(val):
    return val[1]


a.sort(key=fun)
print(a)