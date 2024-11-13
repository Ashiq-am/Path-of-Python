# import inspect library
import inspect

def test(x):
	return x * 2

print(inspect.getsource(test))
