
# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
	print(a, b, c)

# A call with unpacking of dictionary
d = {'a':2, 'b':4, 'c':10}
fun(**d)






"""Here ** unpacked the dictionary used with it, and passed the items in the dictionary as keyword arguments to the function. 
So writing “fun(1, **d)” was equivalent to writing “fun(1, b=4, c=10)”."""




# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):

	# kwargs is a dict
	print(type(kwargs))

	# Printing dictionary items
	for key in kwargs:
		print("%s = %s" % (key, kwargs[key]))

# Driver code
fun(name="geeks", ID="101", language="Python")






"""Applications and Important Points

1. Used in socket programming to send a vast number of requests to a server.

2. Used in Django framework to send variable arguments to view functions.

3. There are wrapper functions that require us to pass in variable arguments.

4. Modification of arguments become easy, but at the same time validation is not proper, 
so they must be used with care."""