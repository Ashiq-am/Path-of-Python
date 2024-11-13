# Python code to demonstrate issubclass()
class A():
	def __init__(self, a):
			self.a = a
class B(A):
	def __init__(self, a, b):
			self.b = b
			A.__init__(self, a)

print(issubclass(B, A))
