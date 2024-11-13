def dict_from_func(func):
	return {func.__name__: func}


activity = {}

@activity.update
@dict_from_func
def mul(a, b):
	return a * b


@activity.update
@dict_from_func
def add(a, b):
	return a + b


print(mul)
print(activity)
print(activity['mul'](2, 5))
