# Python code to remove all the
# sublist outside the given range

# Initialisation of list of list
list = [[0,1.2,3.4,18.1,10.1],
		[10.3,12.4,15,17,16,11],
		[1000,100,10,3.2,11,13, 17.1], ]

# Defining range
left, right = 10, 17

# initialization of index
b=0

for t in list:
	a=0
	for k in t:
		if k<left or k>right:
			a=1
	if a==1:
		list.pop(b)
	b=b+1

# printing output
print(list)
