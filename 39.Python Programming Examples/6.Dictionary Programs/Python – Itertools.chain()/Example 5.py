from itertools import chain

li = ['ABC', 'DEF', 'GHI', 'JKL']

# using chain-single iterable.
res1 = list(chain(li))


res2 = list(chain.from_iterable(li))

print("using chain :", res1, end ="\n\n")

print("using chain.from_iterable :", res2)
