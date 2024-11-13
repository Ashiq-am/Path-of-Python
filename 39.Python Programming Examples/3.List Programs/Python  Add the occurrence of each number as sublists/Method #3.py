# Python program to add the occurrence
# of each number as sublists using counter() method

from collections import Counter
def count_occurence(l):
	c = Counter(l)
	l1 = []
	for k,v in c.items():
		l1.append([k,v])
	return l1


# Driver code
l = [3, 5, 7, 2, 3, 5, 9.1]
print(count_occurence(l))
