# Python code to create pair of element
# from two list such that element
# in pairs are not equal.

# List initialization
list1 =[10, 20, 30, 40]
list2 =[40, 50, 60]

# using list comprehension
output = [[a, b] for a in list1
		for b in list2 if a != b]

# printing output
print(output)
