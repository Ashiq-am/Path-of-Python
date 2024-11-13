class Student:
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

S1 = Student (58, 60)
S2 = Student (60, 58)

# this will generate an error
S3 = S1 + S2
