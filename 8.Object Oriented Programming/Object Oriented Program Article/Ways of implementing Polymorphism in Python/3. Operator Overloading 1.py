class Student:

	# defining init method for class
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	# overloading the + operator
	def __add__(self, other):
		m1 = self.m1 + other.m1
		m2 = self.m2 + other.m2
		s3 = Student(m1, m2)
		return s3

s1 = Student(58, 59)
s2 = Student(60, 65)
s3 = s1 + s2
print(s3.m1)
