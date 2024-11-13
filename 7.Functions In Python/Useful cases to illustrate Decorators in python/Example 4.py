# Creating a decorator
class function_1:
	def __init__(self, func):
		self.func = func
		self.stats = []

	def __call__(self, *args, **kwargs):
		try:
			result = self.func(*args, **kwargs)
		except Exception as e:
			self.stats.append((args, kwargs, e))
			raise e
		else:
			self.stats.append((args, kwargs, result))
			return result

	@classmethod
	def function_2(cls, func):
		return cls(func)


@function_1.function_2
def func(x, y):
	return x / y

print(func(6, 2))

print(func(x = 6, y = 4))

func(5, 0)
print(func.stats)
print(func)
