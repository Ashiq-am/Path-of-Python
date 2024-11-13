# Python3 code to demonstrate working of
# Find dictionary matching value in list
# Using list() + dictionary comprehension

# Initialize list
test_list = [{'gfg' : 2, 'is' : 4, 'best' : 6},
			{'it' : 5, 'is' : 7, 'best' : 8},
			{'CS' : 10, 'is' : 8, 'best' : 10}]

# Printing original list
print("The original list is : " + str(test_list))

# Initialize K
K = 6

# Using list() + dictionary comprehension
# Find dictionary matching value in list
res = list((sub for sub in test_list if sub['is'] >= K))

# printing result
print("The filtered dictionary records : " + str(res))
