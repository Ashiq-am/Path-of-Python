from itertools import chain

li = ['123', '456', '789']

res = list(map(int, list(chain.from_iterable(li))))

sum_of_li = sum(res)

print("res =", res, end ="\n\n")
print("sum =", sum_of_li)
