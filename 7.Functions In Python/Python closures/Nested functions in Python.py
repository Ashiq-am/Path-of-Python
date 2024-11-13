"""A function which is defined inside another function is known as nested function.
Nested functions are able to access variables of the enclosing scope.

In Python, these non-local variables can be accessed only within their scope and not outside their scope.
This can be illustrated by following example:"""




# Python program to illustrate
# nested functions
def outerFunction(text):
	text = text

	def innerFunction():
		print(text)

	innerFunction()

if __name__ == '__main__':
	outerFunction('Hey!')







'''As we can see innerFunction() can easily be accessed inside the outerFunction body but not outside of it’s body. 
Hence, here, innerFunction() is treated as nested Function which uses text as non-local variable.'''