def func(a, b, c='geeks'):
	print(a, "type is", type(a))
	print(b, "type is", type(b))
	print(c, "type is", type(c))


# The optional parameters will not decide
# the type of parameter passed.
# also the order is maintained
print("first call")
func(2, 'z', 2.0)

# below call uses the default
# mentioned value of c
print("second call")
func(2, 1)

# The below call (in comments) will give an error
# since other required parameter is not passed.
# func('a')
print("third call")
func(c=2, b=3, a='geeks')
