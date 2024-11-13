# function
def foo(a, b, c=10):
	print('a =', a)
	print('b =', b)
	print('c =', c)


# call the functions
print("Function Call 1")
foo(2, 3, 8)
print("Function Call 2")
foo(2, 3)
print("Function Call 3")
foo(a=2, c=3, b=10)
