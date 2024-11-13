# Python program to demonstrate
# passing of multiple iterable arguments to map()
# using 3 lists

# Function which return product of 2 numbers
def Multiply(a,b,c):
	return a*b*c

# list 1
lst1=[2,4,6,8,10,12,14,16]

# list 2
lst2=[1,3,5,7,9,11,15]

#list 3
lst3=[2,3,5,7,11,13,17]


result=list(map(Multiply,lst1,lst2,lst3))
print(result)
