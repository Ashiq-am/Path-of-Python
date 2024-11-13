#In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside.


class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)

    # Driver code


myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
print(myObject.__hiddenVariable)



#In the above program, we tried to access hidden variable outside the class using object and it threw an exception.







#We can access the value of hidden attribute by a tricky syntax:


# A Python program to demonstrate that hidden
# members can be accessed outside a class
class MyClass:

	# Hidden member of MyClass
	__hiddenVariable = 10

# Driver code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)





