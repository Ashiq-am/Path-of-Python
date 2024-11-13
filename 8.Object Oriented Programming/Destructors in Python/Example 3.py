# Python program to illustrate destructor

class A:
	def __init__(self, bb):
		self.b = bb

class B:
	def __init__(self):
		self.a = A(self)
	def __del__(self):
		print("die")

def fun():
	b = B()

fun()



#In this example when the function fun() is called, it creates an instance of class B which passes itself to class A,
# which then sets a reference to class B and resulting in a circular reference.