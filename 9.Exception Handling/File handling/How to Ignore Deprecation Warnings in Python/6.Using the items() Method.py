import collections

d = collections.OrderedDict([('a', 1), ('b', 2)])
for key, value in d.items():
	print(key, value)
