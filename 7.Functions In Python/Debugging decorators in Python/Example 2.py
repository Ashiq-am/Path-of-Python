# decorator
def make_geek_happy(func):
	def wrapper():
		neutral_message = func()
		happy_message = neutral_message + " You are happy!"
		return happy_message
	return wrapper

#using the decorator
@make_geek_happy
def speak():
	"""Returns a neutral message"""
	return "Hi, Geeks!"

print(speak())
