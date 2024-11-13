# Replace Values in a List using While Loop

# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

i = 0
while i < len(l):

	# replace hardik with shardul
	if l[i] == 'Hardik':
		l[i] = 'Shardul'

	# replace pant with ishan
	if l[i] == 'Pant':
		l[i] = 'Ishan'

	i += 1

# print list
print(l)
