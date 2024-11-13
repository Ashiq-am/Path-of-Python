def myFun(x, arr):
	print("Inside function")

	# changing integer will
	# Also change the reference
	# to the variable
	x += 10
	print("Value received", x, "Id", id(x))

	# Modifying mutable objects
	# will also be reflected outside
	# the function
	arr[0] = 0
	print("List received", arr, "Id", id(arr))

# Driver's code
x = 10
arr = [1, 2, 3]

print("Before calling function")
print("Value passed", x, "Id", id(x))
print("Array passed", arr, "Id", id(arr))
print()

myFun(x, arr)

print("\nAfter calling function")
print("Value passed", x, "Id", id(x))
print("Array passed", arr, "Id", id(arr))
