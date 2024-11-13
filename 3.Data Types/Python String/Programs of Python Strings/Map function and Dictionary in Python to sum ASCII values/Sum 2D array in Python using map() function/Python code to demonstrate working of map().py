# Python code to demonstrate working of map()

# Function to calculate square of any number
def calculateSquare(n):
	return n*n

# numbers is a list of elements
numbers = [1, 2, 3, 4]

# Here map function is mapping calculateSquare
# function to each element of numbers list.
# It is similar to pass each element of numbers
# list one by one into calculateSquare function
# and store result in another list
result = map(calculateSquare, numbers)

# resultant output will be [1,4,9,16]
print (result)
