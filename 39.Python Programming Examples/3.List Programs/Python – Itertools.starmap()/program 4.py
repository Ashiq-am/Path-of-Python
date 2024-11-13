from itertools import starmap

li =[(2, 3), (3, 1), (4, 6), (5, 3), (6, 5), (7, 2)]

ans = list(starmap(lambda x, y:x + y, li))

print(ans)
