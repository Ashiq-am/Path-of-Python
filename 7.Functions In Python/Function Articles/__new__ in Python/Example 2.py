# Python program to
# demonstrate __new__

class A(object):
	def __new__(cls):
		print("Creating instance")

	# It is not called
	def __init__(self):
		print("Init is called")

print(A())
