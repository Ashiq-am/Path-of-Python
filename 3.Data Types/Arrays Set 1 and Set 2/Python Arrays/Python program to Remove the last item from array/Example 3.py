import array as a

# initializes array with signed
# integers
arr = a.array('i', [1, 2, 3, 4, 5])

# printing original array
print("The original array is : ", end="")
for i in arr:
	print(i, end=" ")
print()

# using pop() to remove element at
# the last position
print("The popped element is : ", end="")
print(arr[-1])
del arr[-1]

print("The array after removing last element is : ", end="")
for i in arr:
	print(i, end=" ")
print()
