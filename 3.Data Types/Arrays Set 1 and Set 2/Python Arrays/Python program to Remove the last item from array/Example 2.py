# importing array from array module
import array as a

# initializes array with signed integers
arr = a.array('i', [1, 2, 3, 4, 5])

# printing original array
print("The original array is : ", end="")
for i in range(0, 5):
	print(arr[i], end=" ")
print()

# using pop() to remove element at
# the last position
print("The popped element is : ", end="")
print(arr.pop())
print("The array after removing last element is : ",
	end="")

for i in range(0, 4):
	print(arr[i], end=" ")
print()
