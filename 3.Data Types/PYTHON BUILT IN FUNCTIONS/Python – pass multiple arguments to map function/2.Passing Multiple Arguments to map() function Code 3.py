# Python program to demonstrate
# passing of multiple iterable arguments to map()
# using list and tuple

# Function which perform division of 2 numbers
def division(a,b):
	return a/b

# list
lst=[2,4,6,8,10,12,14,16]

# tuple
tup=(2,3,5,7,9,11)

result=list(map(division,lst,tup))
print(result)
