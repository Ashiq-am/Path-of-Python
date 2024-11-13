# Replace Values in a List using For Loop

# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

for i in range(len(l)):

	# replace hardik with shardul
	if l[i] == 'Hardik':
		l[i] = 'Shardul'

	# replace pant with ishan
	if l[i] == 'Pant':
		l[i] = 'Ishan'

# print list
print(l)
