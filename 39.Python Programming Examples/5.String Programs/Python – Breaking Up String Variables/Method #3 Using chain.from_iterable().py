from itertools import chain


a = "GeeksForGeeks"

# using chain.from_iterable()
# to convert list of string and characters
# to list of characters
res = list(chain.from_iterable(a))

# printing result
print(str(res))
