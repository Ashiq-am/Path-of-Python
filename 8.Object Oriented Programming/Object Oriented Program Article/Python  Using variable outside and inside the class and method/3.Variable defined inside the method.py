# Program to demonstrate 'Variable
# defined inside the method'

# print("Inside_method1", inVar) # Error

'''class one'''
class Geek:
	print()
# print("Inside_method2", inVar) # Error

	def access_method(self):

		# Variable defined inside the method.
		inVar = 'inside_method'
		print("Inside_method3", inVar)

uac = Geek()
uac.access_method()

'''class two'''
class AnotherGeek:
	print()
# print("Inside_method4", inVar) # Error

	def access_method(self):
		print()
# print("Inside_method5", inVar) # Error

uaac = AnotherGeek()
uaac.access_method()
