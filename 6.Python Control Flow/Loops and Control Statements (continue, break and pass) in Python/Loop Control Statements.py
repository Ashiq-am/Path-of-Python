"""Continue Statement"""




# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
	if letter == 'e' or letter == 's':
		continue
	print('Current Letter :', letter)
	var = 10











'''Break Statement'''


for letter in 'geeksforgeeks':

	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'e' or letter == 's':
		break

print('Current Letter :', letter)







'''Pass Statement'''



# An empty loop
for letter in 'geeksforgeeks':
	pass
print('Last Letter :', letter)


