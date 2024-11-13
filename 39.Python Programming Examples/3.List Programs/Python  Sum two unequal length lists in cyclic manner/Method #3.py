# Python code to add two different
# length lists in cyclic manner

# List initialization
list1 = [150, 177, 454, 126]
list2 = [9, 44, 2, 168, 66, 80, 123, 6, 180, 184]

# List comprehension
output = [list1[i % len(list1)]+list2[i]
			for i in range(len(list2))]

# Printing output
print(output)
