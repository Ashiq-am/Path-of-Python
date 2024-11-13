# Python program to demonstrate
# empty class


class Employee:
	pass


# Driver's code
# Object 1 details
obj1 = Employee()
obj1.name = 'Nikhil'
obj1.office = 'GeeksforGeeks'

# Object 2 details
obj2 = Employee()
obj2.name = 'Abhinav'
obj2.office = 'GeeksforGeeks'
obj2.phone = 1234567889


# Printing details
print("obj1 Details:")
print("Name:", obj1.name)
print("Office:", obj1.office)
print()

print("obj2 Details:")
print("Name:", obj2.name)
print("Office:", obj2.office)
print("Phone:", obj2.phone)


# Uncommenting this print("Phone:", obj1.phone)
# will raise an AttributeError
