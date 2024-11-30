from operator import itemgetter

a = [1, 'geeks', 3, 'for', 5]

a1 = itemgetter(1, 3)(a)
print(a1)