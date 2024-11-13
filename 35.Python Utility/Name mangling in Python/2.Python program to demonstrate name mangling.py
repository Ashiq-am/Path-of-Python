# Python program to demonstrate
# name mangling


class Student:
	def __init__(self, name):
		self.__name = name

s1 = Student("Santhosh")
print(dir(s1))
