def comp(a, b=2):
	if(a < b):
		print("first parameter is smaller")
	if(a > b):
		print("second parameter is smaller")
	if(a == b):
		print("both are of equal value.")


print("first call")
comp(1)
print("second call")
comp(2, 1)
print("third call")
comp(b=1, a=-1)
print("fourth call")
comp(-1, b=0)
