class A:
	def __init__(self):
		print('Class - A Constructor')

	def m1(self):
		print('M1 method of Class - A.')


class B:
	def __init__(self):
		print('Class - B Constructor.')

	# instance method
	def m2(self):

		# creating object of class A inside
		# B class instance method
		obj = A()

		# calling m1() method of class-A
		obj.m1()
		print('M2 method of Class - B.')


# creating object of class-B
obj = B()

# calling B class m2() method
obj.m2()
