# Python code to find number of list in a tuple

# Using find function
def find(Input):
	if isinstance(Input, list):
		return 1
	else:
		return len(Input)

# List initialization
Input1 = ([1, 2, 3, 4], [5, 6, 7, 8])
Input2 = ([1, 2], [3, 4], [5, 6])
Input3 = ([9, 8, 7, 6, 5, 4, 3, 2, 1])

# using find
Output1 = find(Input1)
Output2 = find(Input2)
Output3 = find(Input3)

# printing
print("Initial list :")
print(Input1)
print("No of list in tuples are :")
print(Output1)
print("\n")

print("Initial list :")
print(Input2)
print("No of list in tuples are :")
print(Output2)
print("\n")


print("Initial list :")
print(Input3)
print("No of list in tuples are :")
print(Output3)
print("\n")
