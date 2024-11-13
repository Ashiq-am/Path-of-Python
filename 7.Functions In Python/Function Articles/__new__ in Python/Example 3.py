# Python program to
# demonstrate __new__

class A(object):
	# new method returning a string
	def __new__(cls):
		print("Creating instance")
		return "GeeksforGeeks"

class B(object):
	# init method returning a string
	def __init__(self):
		print("Initializing instance")
		return "GeeksforGeeks"

print(A())
print(B())
