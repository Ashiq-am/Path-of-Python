# Python program to
# verify pass by reference

def myFun(x):
	print("Value recieved:", x, "id:", id(x))

# Driver's code
x = 12
print("Value passed:", x, "id:", id(x))
myFun(x)
