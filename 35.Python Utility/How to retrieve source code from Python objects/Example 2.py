# import inspect library
import inspect


def far(n):
	factorial = 1
	if int(n) >= 1:
		for i in range (1, int(n)+1):
			factorial = factorial * i
	return factorial

source = inspect.getsource(far)
print(source)
