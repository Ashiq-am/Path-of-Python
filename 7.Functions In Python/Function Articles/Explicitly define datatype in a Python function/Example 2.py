# function definition
def concatenate(num1, num2):
	print("Datatype of num1 is ", type(num1))
	print("Datatype of num2 is ", type(num2))
	return num1 + num2

# calling the function without
# explicitly declaring the datatypes
print(concatenate(111, 100))

# calling the function by explicitly
# defining the datatype as float
print(concatenate(str(111), str(100)))
