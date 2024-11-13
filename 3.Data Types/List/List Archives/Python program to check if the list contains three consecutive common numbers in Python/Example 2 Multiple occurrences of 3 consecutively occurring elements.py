# creating the array
arr = [1, 1, 1, 64, 23, 64, 22, 22, 22]

# size of the list
size = len(arr)

# looping till length - 2
for i in range(size - 2):

	# checking the conditions
	if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:

		# printing the element as the
		# conditions are satisfied
		print(arr[i])
