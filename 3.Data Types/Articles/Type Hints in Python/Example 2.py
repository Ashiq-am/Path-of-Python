# factorial function
def factorial(i: int) -> int:
if i<0:
	return None
if i == 0:
	return 1
return i * factorial(i-1)

# passing a fraction to the function
print(factorial(5.01))
