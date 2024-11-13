# Python code to demonstrate the working of
# compress()



import itertools
import operator


example = itertools.compress('ABCDE', [1, 0, 1, 0, 0])

for each in example:
	print(each)
