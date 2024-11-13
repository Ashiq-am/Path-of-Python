# A Python program to demonstrate use
# of packing

# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
	sum = 0
	for i in range(0, len(args)):
		sum = sum + args[i]
	return sum

# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))





'''The above function mySum() does ‘packing’ to pack all the arguments that this method call receives into one 
single variable. Once we have this ‘packed’ variable, we can do things with it that we would with a normal tuple. 
args[0] and args[1] would give you the first and second argument, respectively. Since our tuples are immutable, 
you can convert the args tuple to a list so you can also modify, delete and re-arrange items in i.'''



