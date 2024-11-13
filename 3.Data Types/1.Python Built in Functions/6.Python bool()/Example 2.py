# Python code to check whether a number
# is even or odd using bool()

def check(num):
	return(bool(num % 2 == 0))

# Driver Code
num = 8
if(check(num)):
	print("Even")
else:
	print("Odd")
