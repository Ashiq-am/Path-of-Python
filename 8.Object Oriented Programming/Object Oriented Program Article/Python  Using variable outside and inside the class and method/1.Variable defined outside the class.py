# Program to demonstrate 'Variable
# defined outside the class'

# Variable defined outside the class.
outVar = 'outside_class'
print("Outside_class1", outVar)

''' Class one '''
class Geek:
	print("Outside_class2", outVar)

	def access_method(self):
		print("Outside_class3", outVar)

# Calling method by creating object
uac = Geek()
uac.access_method()

''' Class two '''
class Another_Geek_class:
	print("Outside_class4", outVar)

	def another_access_method(self):
		print("Outside_class5", outVar)

# Calling method by creating object
uaac = Another_Geek_class()
uaac.another_access_method()
