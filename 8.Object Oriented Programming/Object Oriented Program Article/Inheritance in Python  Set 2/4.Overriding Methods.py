# Base Class
class A(object):
		def __init__(self):
				constant1 = 1
		def method1(self):
				print('method1 of class A')

class B(A):
		def __init__(self):
				constant2 = 2
				self.calling1()
				A. __init__(self)
		def method1(self):
				print('method1 of class B')
		def calling1(self):
				self.method1()
				A.method1(self)
b = B()
