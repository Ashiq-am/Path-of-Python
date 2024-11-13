# Python program to illustrate
# callable()
# a test function
def Geek():
	return 5

# an object is created of Geek()
let = Geek
print(callable(let))

# a test variable
num = 5 * 5
print(callable(num))
