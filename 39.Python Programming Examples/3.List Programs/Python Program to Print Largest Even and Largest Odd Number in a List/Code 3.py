# Python program for the above approach

def printmax(lis):

	# Using list comprehension storing
	# even and odd numbers as separate lists
	even = [x for x in lis if x % 2 == 0]
	odd = [x for x in lis if x % 2 == 1]

	# printing max numbers in corresponding lists
	print("Largest odd number is ", max(odd))
	print("Largest even number is ", max(even))


# Input a list of numbers
lis = [123, 234, 236, 694, 809]

printmax(lis)

