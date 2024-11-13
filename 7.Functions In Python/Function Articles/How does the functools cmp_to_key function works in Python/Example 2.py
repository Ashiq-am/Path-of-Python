import functools


def mycmp(a, b):
	print("comparing ", a, " and ", b)
	if a > b:
		return 1
	elif a < b:
		return -1
	else:
		return 0


print(min([45, 78, 813], key=functools.cmp_to_key(mycmp)))
print(max([45, 78, 813], key=functools.cmp_to_key(mycmp)))
