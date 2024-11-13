# class addition
class addition:
	def __init__(self):
		self.a = 10
		self.b = 10

	# defining __str__() function
	def __str__(self):
		return 'value of a = {} value of b = {}'.format(self.a, self.b)

# creating object ad
ad = addition()
print(str(ad))

# printing the type
print(type(str(ad)))
