# Python program to show working
# of map() function

# Return cube of n
def cube(n):
	return n**3

# Taking list as iterator
evennum = [2,4,6,8]
res = map(cube,evennum)
print(list(res))
