# Python code to demonstrate
# the working of the sharing
# of data variables

# Creating a class inside __init__
class Geek_Class:
	def __init__(self):
		self.geek = []

x = Geek_Class()
y = Geek_Class()

# Apending the values
x.geek.append(1)
y.geek.append(2)
x.geek.append(3)
y.geek.append(4)

# Printing the values for x and y
print(x.geek)
print(y.geek)
