# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)




'''Return sends a specified value back to its caller whereas Yield can produce a sequence of values. 
We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

Yield are used in Python generators. A generator function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword rather than return. 

If the body of a def contains yield, the function automatically becomes a generator function.'''






# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
	i = 1

	# An Infinite loop to generate squares
	while True:
		yield i*i
		i += 1 # Next execution resumes
				# from this point

# Driver code to test above generator
# function
for num in nextSquare():
	if num > 100:
		break
	print(num)
