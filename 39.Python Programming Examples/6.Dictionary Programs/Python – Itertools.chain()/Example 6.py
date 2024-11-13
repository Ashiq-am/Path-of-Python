from itertools import chain

li = ['123', '456', '789']

res = list(chain.from_iterable(li))

print("res =", res, end ="\n\n")

new_res = list(map(int, res))

print("new_res =", new_res)

sum_of_li = sum(new_res)

print("\nsum =", sum_of_li)
