# Python program to demonstrate
# name mangling


class Student:
	def __init__(self, name):
		self.__name = name

s1 = Student("Santhosh")
print(s1._Student__name)
