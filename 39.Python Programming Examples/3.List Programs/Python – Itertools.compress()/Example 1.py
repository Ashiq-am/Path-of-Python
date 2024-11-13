# Python code to demonstrate the working of
# compress()


import itertools
import operator


Codes =['C', 'C++', 'Java', 'Python']
selectors = [False, False, False, True]

Best_Programming = itertools.compress(Codes, selectors)

for each in Best_Programming:
	print(each)
