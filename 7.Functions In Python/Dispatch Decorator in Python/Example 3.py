from multipledispatch import dispatch


nsp = {}

@dispatch(int, namespace = nsp)
def func(x):
	return x * 2

@dispatch(float, namespace = nsp)
def func(x):
	return x / 2

# Driver code
print(func(2))
print(func(2.0))
print(nsp)
