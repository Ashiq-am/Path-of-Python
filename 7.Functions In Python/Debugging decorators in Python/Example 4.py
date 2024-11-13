# importing the module
import functools

# decorator
def make_geek_happy(func):
	@functools.wraps(func)
	def wrapper():
		neutral_message = func()
		happy_message = neutral_message + " You are happy!"
		return happy_message
	return wrapper

def speak():
	"""Returns a neutral message"""
	return "Hi!"

positive_message = make_geek_happy(speak)
print(positive_message())

print(speak.__name__)
print(speak.__doc__)
print(positive_message.__name__)
print(positive_message.__doc__)
