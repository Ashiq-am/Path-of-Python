# Python program to find sum of list with different
# types.

def calsum(l):

	# returning sum of list using List comprehension
	return sum([int(i) for i in l if type(i)== int or i.isdigit()])

# Declaring list
list1 = [12, 'geek', 2, '41', 'for', 10, '8', 6, 4, 'geeks', 7, '10']
list2 = [100, 'geek', 200, '400', 'for', 101, '2018', 64, 74, 'geeks', 27, '7810']

# Result of sum of list
print (calsum(list1))
print (calsum(list2))
