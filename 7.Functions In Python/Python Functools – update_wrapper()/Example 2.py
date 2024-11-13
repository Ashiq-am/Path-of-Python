import functools


def divide(a, b):
	"Original Documentation of Divide"
	return a / b

half = functools.partial(divide, b = 2)
oneThird = functools.partial(divide, b = 3)

try:
	print(half.__name__)
except AttributeError:
	print('No Name')
print(half.__doc__)
