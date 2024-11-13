# Python code to find if a number is
# prime or not using divmod()

# Given integer
n = 15
x = n

# Initialising counter to 0
count = 0
while x != 0:
	p, q = divmod(n, x)
	x-= 1
	if q == 0:
		count+= 1
if count>2:
	print('Not Prime')
else:
	print('Prime')
