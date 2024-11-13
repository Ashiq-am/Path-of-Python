from itertools import starmap

li =[(2, 5), (3, 2), (4, 3)]

new_li = list(starmap(pow, li))

print(new_li)
