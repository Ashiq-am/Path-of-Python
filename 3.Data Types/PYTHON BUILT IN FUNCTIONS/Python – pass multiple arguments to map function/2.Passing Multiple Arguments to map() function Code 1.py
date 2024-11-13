# Python program to demonstrate
# passing of multiple iterable arguments to map()
# using 2 lists

# Function which return sum of 2 numbers
def sum(a,b):
	return a+b

# list 1
lst1=[2,4,6,8]

# list 2
lst2=[1,3,5,7,9]


result=list(map(sum,lst1,lst2))
print(result)
