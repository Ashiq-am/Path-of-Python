# Python3 code to demonstrate working of
# Remove Equilength and Equisum Tuple Duplicates
# Using dict() + values()

# initializing lists
test_list = [(4, 5, 6), (3, 0), (2, 1), (1, 2, 3), (5, 5, 5)]

# printing original list
print("The original list is : " + str(test_list))

# Remove Equilength and Equisum Tuple Duplicates
# Using dict() + values()
res = list({(len(sub), sum(sub)): sub for sub in test_list}.values())

# printing result
print("Tuples after filteration : " + str(res))
