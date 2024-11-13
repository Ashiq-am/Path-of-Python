numbers = [1, 1, 1, 3, 3, 2, 2, 2, 1, 1]
import itertools
for (key,group) in itertools.groupby(numbers):
	print (key,list(group))
